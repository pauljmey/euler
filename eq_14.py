
def is_power_of(n,f=2):
    if n == f:
        return True

    if n % f == 0:
        return is_power_of(n//f)

    return False

def get_collatz(n):
    ret = [n]

    cur = ret[-1]
    while cur != 1:
        if cur % 2 == 0:
            ret.append(cur//2)
        else:
            ret.append(3*cur + 1)

        cur = ret[-1]

    return ret

test = False
def main(limit=None):

    max = 1
    argmax = 1
    for i in range(1, limit):
        seq = get_collatz(i)
        if len(seq) > max:
            max = len(seq)
            argmax = i

        if i % 1000 == 0 or test:
            print(f"{max}, len= {len(seq)}, cur= {seq}")

    print(f"i is {argmax}, max is {max}")
    return (argmax, max)

if __name__ == "__main__":
    import sys
    main(limit=1000000)
