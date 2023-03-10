
path_lib = {}

def get_path_count(dim):
    def dot(v1, v2):
        return sum(v1[i]*v2[i] for i in range(max(len(v1), len(v2))))

    if dim == 1:
        return 2, [1]

    prev = get_path_count(dim - 1)

    corner_fac = 2
    wing = prev[1]
    side_facs = [1] * dim

    part_1 = corner_fac * prev[0]
    part_1 += 2 * dot(side_facs[1:], wing)
    ret = []
    prev_side = [prev[0]]
    prev_side.extend(wing)

    for i, v in enumerate(prev_side):
        ret.append(dot(side_facs[i:], prev_side[i:]))

    #ret.append(1)

    return part_1, ret



def main(dim=None):
    ret = 0
    for x in range(1, 21):
        print(x, get_path_count(x))

    return ret
'''
q 16
'''
def sum_str(s):
    return sum(int(c) for c in s)

if __name__ == "__main__":
    import sys
    print(main(dim=20))
