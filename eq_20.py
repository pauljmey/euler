
def main(limit=None):
    ret = 1
    for n in range(1, limit + 1):
        if n > 1:
            ret *= n

    print(f"Result is {ret}")
    return ret


if __name__ == "__main__":
    ret = main(limit=100)
    ret = str(ret)
    print(ret)
    nums = [int(c) for c in ret]
    print(sum(nums))