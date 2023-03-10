
def main(limit=None):
    ret = 0
    for n in range(3, limit):
        if n % 3 == 0 or n % 5 == 0:
            ret += n

    print(f"Result is {ret}")
    return ret


if __name__ == "__main__":
    main(limit=1000)