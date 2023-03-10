import math


def main(max=None, min=None):
    def is_palindrome(num):
        def is_palindrome_helper(num_str):
            if len(num_str) < 2:
                return True

            if num_str[0] == num_str[-1]:
                return is_palindrome_helper(num_str[1:-1])

            return False

        return is_palindrome_helper(str(num))

    largest = 0
    for i in range(min, max + 1):
        for j in range(min, max + 1):
            if is_palindrome(i*j):
                if i*j > largest:
                    print(f"i, j = {i},{j}")
                    largest = i * j

    return largest

if __name__ == "__main__":
    print(main(max=999, min=100))