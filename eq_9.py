import math


def main(limit=None):

    for i in range(1,1001):
        for j in range(1, i + 1):
            if i + j >= 1000:
                continue

            c2 = i*i + j*j
            if int(math.sqrt(c2)) == math.sqrt(c2):
                c = int(math.sqrt(c2))
                if i + j + c == 1000:
                    return i + j + c, (i, j, c), i*j*c

    return 0

if __name__ == "__main__":
    print(main(limit=998))