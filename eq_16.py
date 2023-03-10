
import math

def sum_str(s):
    return sum(int(c) for c in s)

num = str(int(math.pow(2,1000)))
print(num)
print(sum_str(num))
