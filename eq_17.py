
import math

def main(limit=10):

    def read_num(x):
        words = []
        if x == 1000:
            words = ['one', 'thousand']
            return words
        elif x < 20:
            words.append (one_up_to_twenty [x - 1])
            return words
        elif x < 100:
            tens_count = x // 10
            words.append(tens[tens_count - 2] )
            if x % 10 == 0:
                return words
            else:
                less_than = read_num(x % 10)
                words.extend(less_than)
                return words
        elif x >= 100:
            huns = x // 100
            hun_words = read_num(huns)
            words.extend(hun_words)
            if x % 100 == 0:
                words.append('hundred')
                return words
            else:
                words.extend(['hundred', 'and'])
                less_than = read_num(x % 100)
                words.extend(less_than)

        return words

    ret = []
    tens =[
        'twenty', 'thirty', 'forty',
        'fifty', 'sixty', 'seventy',
        'eighty', 'ninety'
    ]
    one_up_to_twenty = [
        'one', 'two', 'three',
        'four', 'five', 'six',
        'seven', 'eight', 'nine',
        'ten', 'eleven', 'twelve',
        'thirteen', 'fourteen', 'fifteen',
        'sixteen', 'seventeen', 'eighteen',
        'nineteen'
    ]

    debug_range = [0, 100]
    for x in range(1, limit + 1):
        cur_words = read_num(x)
        #print(cur_words)
        ret.append(cur_words)

    return ret

if __name__ == "__main__":
    import sys
    words = main(limit = 1000)
    count = 0

    for i, w in enumerate(words):
        if i % 5 == 4:
            print(w)
        else:
            print(w, ',', end='')

    checks = {
        9:(1,9),
        19:(10,19),
        99:(20, 99),
        999:(100, 999)
    }
    for i, w in enumerate(words):
        cur_count = [len(cur) for cur in w]

        if i + 1 in [5, 342, 115]:
            print (f"({i + 1}): {w}")
            print(sum(cur_count), ':', cur_count)
        elif i+1 in [9, 19, 99, 999]:
            lb = checks[i+1][0]
            ub = checks[i+1][1]
            cur_check = [row for row in words[lb - 1:ub]]
            print(f"Checking {lb}-{ub}")
            flattened = []
            for r in cur_check:
                flattened.extend(r)

            check_count = [len(curw) for curw in flattened]
            print(f"Checkcount total = {sum(check_count)}")
            print(f"Checkcount vals = {check_count}")




        count += sum(cur_count)
        if i + 1 == 5:
            print(f"current total= {count}")
        #print(w)

    print(f"last {words[-1]}")
    print(count)
