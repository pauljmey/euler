import math

def test_prime(n, primes):

    limit = int(math.sqrt(n))
    for p in primes:
        if p > limit:
            break

        if n % p == 0:
            return p

    return 1


def add_next_prime(primes, limit=None):
    test = primes[-1]
    test += 2
    while True and len(primes) < limit:
        if test_prime(test, primes) == 1:
            primes.append(test)
            #if len(primes) % 100 == 0:
            #    print(f"adding {test}")

            return

        test += 2


def get_base_factors(n, primes):
    base_factors = []

    done = False
    cur = n
    limit = int(n/2)
    limit = max(3, limit)

    if limit > primes[-1]:
        add_next_prime(primes, limit)

    while not done:
        for p in primes:
            if p > limit or cur == 1:
                done = True
                break

            if cur % p == 0:
                base_factors.append(p)
                cur //= p
                break

    return base_factors



def get_tri(pos):
    ret = 0
    for i in range(1, pos + 1):
        ret += i

    return ret

def get_cmd_str(fn, *args, **kwargs):
    ret_str= f"{fn}("
    for i, e in enumerate(args):
        if i > 0:
            ret_str += ', '

        ret_str += args[i]

    for k, v in kwargs.items():
        if ret_str[-1] != "(":
            ret_str += ', '

        ret_str += str(k) + '=' + str(v)

    ret_str += ')'

    return ret_str

def get_factors(base_factors):
    ret = []


    bf = {}
    for f in base_factors:
        if f not in bf:
            bf[f] = 1
        else:
            bf[f] += 1

    sorted_k = sorted(bf)
    complete = sum(bf.values())
    for cnt in range(1, len(sorted_k) + 1):

        if cnt == 1:
            for j in range(bf[sorted_k[0]] + 1):
                ret.append([j])
            continue

        to_add = []
        for a in ret:
            assert (len(a) == cnt - 1)
            for j in range(bf[sorted_k[cnt - 1]] + 1):
                cur = [e for e in a]
                cur.append(j)
                if sum(cur) < complete:
                    to_add.append(cur)

        ret.clear()
        ret.extend(to_add)


    #print(ret)
    ret2 = []
    for v in ret:
        cur = 1
        for i, v2 in enumerate(v):
            if v2 > 0:
                cur *= math.pow(sorted_k[i], v2)

        ret2.append(int(cur))
        ret2 = sorted(ret2)


    restored = 1
    for v in base_factors:
        restored *= v

    ret2.append(restored)

    return ret2

def main(args):
    pargs = []
    kw_args = {}

    if 'args' in args:
        args_index = args.index('args') + 1
    else:
        args_index = None

    if 'kwargs' in args:
        kw_index = args.index('kwargs') + 1
    else:
        kw_index = None

    if not kw_index and not args_index:
        pass
    elif not kw_index:
        pargs = args[args_index:]
        pargs = ''.join(pargs)
        pargs = eval(pargs)
    elif not args_index:
        kw_args = args[kw_index:]
        kw_args = ''.join(kw_args)
        kw_args = eval(kw_args)
    else:

        pargs = args[args_index: kw_index]
        if not pargs:
            kwargs = args[kw_index : args_index]
            pargs = args[args_index: ]
        else:
            kwargs = args[kw_index:]

        if not pargs:
            pass
        else:
            pargs = eval( ''.join(pargs) )

        if not kw_args:
            pass
        else:
            kw_args = eval( ''.join(kw_args) )

    ret = get_cmd_str(args[0], *pargs, **kw_args)

    print(ret)
    test = eval(ret)
    print(test)
    hook = True
    factors_input = [2,2, 3, 3, 5]
    print("base factors ",factors_input)
    ret = get_factors(factors_input)
    for r in ret:
        print(r)

class NumberTriangle:
    def __init__(self, data):
        self._data = [x for x in data]
        self._size = len(self._data)
        last_node = self.node_from_pos(len(self._data) - 1)
        self.last_row = last_node[0]

    def update(self, data):
        assert(len(data) == len(self._data))
        self._data = [x for x in data]

    def row(self, pos):
        if pos == 3:
            hook = True

        nth_row = 0

        while True:
            start_of_next = self.start_of_row(nth_row + 1)
            if start_of_next > pos:
                break
            nth_row += 1

        return nth_row

    def get_row(self, n):
        start_pos = self.start_of_row(n)
        cut_off = None
        if n < self.last_row:
            cut_off = self.start_of_row(n + 1)

        rng_end = cut_off if not cut_off else cut_off - 1

        return self._data[start_pos : cut_off], (start_pos, rng_end)

    def start_of_row(self, nth):
        cur_start = 0
        len = 1
        cur_row = 0
        while cur_row < nth:
            cur_start += len
            len += 1
            cur_row += 1

        return cur_start


    def node_from_pos(self, pos):
        nth_row = self.row(pos)
        cur_start = self.start_of_row(nth_row)
        offset = pos - cur_start
        return nth_row, offset

    def pos_from_node(self, nd):
        if not nd:
            hook = True

        return self.start_of_row(nd[0]) + nd[1]

    def offset(self, pos):
        cur_row = self.row(pos)
        return pos - self.start_of_row(cur_row)

    def left(self, pos):
        cur_row, cur_offset = self.node_from_pos(pos)

        cur_start = self.start_of_row(cur_row)
        next_start = self.start_of_row(cur_row + 1)
        offset = cur_offset

        return next_start + offset

    def right(self, pos):
        return self.left(pos) + 1

    def parent_nodes(self, pos):
        r = l = None
        if pos == 0:
            return (l, r)
        cur_row, cur_offset = self.node_from_pos(pos)
        cur_last_offset = cur_row

        if cur_offset < cur_last_offset:
            r = (cur_row - 1, cur_offset)

        if cur_offset > 0:
            l = (cur_row - 1, cur_offset - 1)

        return (l, r)

    def pos(self, r, off=None):
        offset = 0
        if off is not None:
            offset = off
        s_pos = self.start_of_row(r)
        return  s_pos + offset

    def left_branch(self, pos):
        _, cur_offset = self.node_from_pos(pos)
        ret = [
            (pos + i, val) for i, val in enumerate(self._data[pos:])
                if cur_offset == self.offset(pos + i)
        ]

        return ret


    def right_branch(self, pos):
        def check(i):
            return cur_offset == self.offset(i) - (self.row(i) - cur_row)

        cur_row, cur_offset = self.node_from_pos(pos)
        ret = [
            #(i, val, self.row(i), self.offset(i), cur_offset == self.offset(i) - (self.row(i) - cur_row)) for i, val in enumerate(self._data[pos:])
            (i, val) for i, val in enumerate(self._data[pos:]) if check(i)
        ]

        return ret

    def print(self):
        for r in range(self.last_row + 1):
            cells, rng = self.get_row(r)
            if not rng:
                rng_str = "none"
            else:
                rng_str = f' {rng[0]}-{rng[1]}'

            print(r, ':', cells, rng_str)


if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
