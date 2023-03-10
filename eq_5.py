import math

def gcf(n, m):
    vals = [n, m]
    larger = 1
    smaller = 0

    if vals[larger] < vals[smaller]:
        larger = 0
        smaller = 1

    diff = vals[larger] - vals[smaller]



    return gcf(diff, vals[smaller])




def main(num):
    # table = [[0] * 31 for i in range(0, 31)]
    # for i in range(len(table)):
    #     table[i][0] = i
    #     table[0][i] = i
    #
    # for i in range(1, 31):
    #     for j in range(1, 31):
    #         res = gcf(i, j)
    #         table[i][j] = res
    #
    # for r in table:
    #     print([f"{v:2}" for v in r])

    ret = 1
    added = []

    ret = 20
    to_add = [n for n in range(2,20)]
    added = [4, 5]
    for candidate in to_add:
        init_val = candidate
        temp = ret
        if temp % candidate == 0:
            continue

        for pre in added:
            if candidate % pre == 0:
                candidate = candidate // pre
                temp = temp // pre

        if temp % candidate != 0:
            print(f"adding {candidate} for {init_val}")
            ret *= candidate
            print(f"new ret = {ret}")
            added.append(candidate)

    print("added = {added}")
    return ret

if __name__ == "__main__":
    ret = main(num=20)
    print(ret)

    for n in range(2, 20):
        print(f"{n}, {ret / n}")