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
            if len(primes) % 100 == 0:
                print(f"adding {test}")

            return

        test += 2



def get_lpf(num,sto=[]):

    limit = int(math.sqrt(num))

    if not sto:
        sto.append(2)
        sto.append(3)

    last = sto[-1]

    offset = 2
    cur_index = 0
    while True:
        p = sto[cur_index]

        if num % p == 0:
            print(f"Factor pair is {p}, {num // p}")
            factor_lpf = get_lpf(num // p)
            if factor_lpf > p:
                print(f"returning {factor_lpf} for {num}, other factor = {p}")
                return factor_lpf
            else:
                print(f"returning {p} for {num}, other factor = {factor_lpf}")
                return p

        cur_index += 1
        if p == last and p <= limit:
            add_next_prime(sto)
            last = sto[-1]
        elif p > limit:
            break

    return num

def main(stop=None):
    def is_prime(n, primes):
        limit = int(math.sqrt(n))
        for p in primes:
            if p > limit:
                break
            else:
                if p == n:
                    return True

                if n % p == 0:
                    return False

        return True

    primes = [2, 3]
    limit = math.sqrt(2000000)
    while primes[-1] < limit:
        add_next_prime(primes, stop)

    ret = 2
    for n in range(3, 2000001, 2):
        if is_prime(n, primes):
            ret += n
            print(f'adding {n}')

    print(f'sum is {ret}')


if __name__ == "__main__":
    main(stop=10001)