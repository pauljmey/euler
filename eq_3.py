import math

def get_lpf(num,sto=[]):
    def test_prime(n, primes):
        ret = 1
        for p in primes:
            if n % p == 0:
                return p

        return ret

    def add_next_prime(primes):
        test = primes[-1]
        while True:
            if test_prime(test, primes) == 1:
                primes.append(test)
                if len(primes) % 100 == 0:
                    print(f"adding {test}")

                return
            test += 2


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

def main(num=None):
    print(get_lpf(num))

if __name__ == "__main__":
    main(num=600851475143)