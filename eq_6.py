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




def main(num=None):
    vals = [n for n in range(1, num + 1)]
    ret = 0
    for i, v in enumerate(vals):
        for j, v2 in enumerate(vals):
            if j != i:
                ret += vals[i] * vals[j]

    return ret

if __name__ == "__main__":
    ret = main(num=100)
    print(ret)

