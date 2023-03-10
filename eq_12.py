import math
from utils import test_prime, get_base_factors, get_factors, get_tri


def main(num_factors=None):

    done = False
    pos = 1
    primes = [2,3,5,7,11]
    while not done:

        cur_tri = get_tri(pos=pos)
        pos += 1
        #if pos > 10:
        #    break
        if cur_tri == 28:
            hook = True
        p_factors = get_base_factors(cur_tri, primes)
        cur_f = get_factors(p_factors)
        if len(cur_f) % 10 == 0 or cur_tri < 100 or pos % 1000 == 0 :
            print(p_factors)
            print(cur_f)
            print(f"tri = {cur_tri}, num factors = {len(cur_f)} ")

        if len(cur_f) > num_factors:
            print("prime factors", p_factors)
            print("all factors:")
            for i in range(0, len(cur_f), 15):
                print(f"{i}-{i+14}>{cur_f[i:i+15]}")

            print(f"{pos}: tri = {cur_tri}, num factors = {len(cur_f)} ")
            break



if __name__ == "__main__":
    import sys

    main(num_factors=int(sys.argv[1]))

