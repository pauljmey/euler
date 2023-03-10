coins = [1, 2, 5, 10, 20, 50, 100, 200]

def main(limit=None):
    def make_change_v(new_coin, old=None):
        if not old:
            old = tuple([0 for x in coins])

        idx = coins.index(new_coin)
        new_v = [x for x in old]
        new_v[idx] += 1
        return tuple(new_v)

    def get_available(amt):
        return [c for c in coins if c <= amt]

    ret = None
    cv = make_change_v(1)
    table = [limit * [ [0, []] ] for x in range(limit)]

    table[0][0] = [1, [cv]]
    for ri, r in enumerate(table):
        if ri == 0:
            continue
        amount = ri + 1

        for ci, c in enumerate(table[ri]):
            coins_to_use = ci + 1
            available = get_available(amount)
            for ac in available:
                if ci == 0:
                    if amount in available:
                        cv = make_change_v(ac)
                        table[ri][ci] = [1,[cv]]
                elif ri - ac < 0:
                    continue
                else:
                    cur_vs = table[ri][ci][1]
                    if table[ri - ac][ci - 1][0] > 0:
                        old = table[ri - ac][ci - 1][1]
                        to_test = [make_change_v(ac,old=o) for o in old]
                        for v in to_test:
                            if v in cur_vs:
                                pass
                            else:
                                table[ri][ci][0] += 1
                                table[ri][ci][1].append(v)
                                cur_vs = cur_vs = table[ri][ci][1]

    ret = table

    return ret


if __name__ == "__main__":
    table = main(limit=200)
    hook = True