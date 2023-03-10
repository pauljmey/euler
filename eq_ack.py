
def main(limit=None):
    def get_val(m, n):
        def check(m, n):

        if m < len(table) and n < len(table[0]) and  table[m, n] != -1:
            return table[m, n]

        if m == 0:
            if n is None:
                hook = True

            table[m, n] = n + 1
            return n + 1
        elif n == 0:
            return table[m-1][1]
        elif n >= limit or table[m - 1][n] == -1:
            n2 = get_val(m, n - 1)
            return get_val(m - 1, n2)
        else:
            print(m,n)
            n2 = table[m][n - 1]
            if n2 >= limit or table[m - 1][n2] == -1:
                return get_val(m - 1, get_val(m, n - 1))
            else:
                ret = -1
                try:
                    ret = table[m-1][n2]
                except IndexError as ex:
                    hook = True

                if ret == -1 or ret is None:
                    hook = True

                return ret



    table = [[-1] * (limit+1) for x in range(limit + 1)]
    for ci, _ in enumerate(table[0]):
        table[0][ci] = ci + 1

    ret = table


    for ci in range(len(table[0])):
        for ri in range(len(table)):
            m = ri
            n = ci
            if ci > 0:
                hook = True
            table[m][n] = get_val(m,n)

        if ci > 0:
            for r in table:
                print(r)

    return ret


if __name__ == "__main__":
    ret = main(limit=10)
    for x in ret:
        print(x)