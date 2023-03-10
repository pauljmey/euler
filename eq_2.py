
def main(largest=None):
    ret = 2
    n_2 = 1
    n_1 = 2
    n = 3
    while n <= 4000000:
        if n % 2 == 0:
            ret += n
        n_2 = n_1
        n_1 = n
        n = n_1 + n_2

    print(f"Result is {ret}")
    return ret


if __name__ == "__main__":
    main(largest=4000000)