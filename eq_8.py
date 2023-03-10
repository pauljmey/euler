import math

big_num = "73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450"

def test_prime(n, primes):

    limit = int(math.sqrt(n))
    for p in primes:
        if p > limit:
            break

        if n % p == 0:
            return p

    return 1


def add_next_prime(primes, limit=None):
    test = primes[-1]
    test += 2
    while True and len(primes) < limit:
        if test_prime(test, primes) == 1:
            primes.append(test)
            if len(primes) % 100 == 0:
                print(f"adding {test}")

            return

        test += 2



def get_lpf(num,sto=[]):

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
    print(num)
    print(int(num))
    largest = 1
    for i, v in enumerate(num):
        if len(num[i:]) < 13:
            break

        cur = 1
        for j in num[i: i+13]:
            cur *= int(j)

            if cur > largest:
                largest = cur
                print(largest)



if __name__ == "__main__":
    main(num=big_num)