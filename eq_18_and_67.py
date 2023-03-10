from utils import NumberTriangle

triangle = [
    75, 95, 64, 17, 47, 
    82, 18, 35, 87, 10, 
    20, 4, 82, 47, 65,
    19, 1, 23, 75, 3,
    34, 88, 2, 77, 73,
    7, 63, 67, 99, 65,
    4, 28, 6, 16, 70,
    92, 41, 41, 26, 56,
    83, 40, 80, 70, 33,
    41, 48, 72, 33, 47,
    32, 37, 16, 94, 29,
    53, 71, 44, 65, 25,
    43, 91, 52, 97, 51,
    14, 70, 11, 33, 28,
    77, 73, 17, 78, 39,
    68, 17, 57, 91, 71,
    52, 38, 17, 14, 91,
    43, 58, 50, 27, 29,
    48, 63, 66, 4, 68,
    89, 53, 67, 30, 73,
    16, 69, 87, 40, 31,
    4, 62, 98, 27, 23,
    9, 70, 98, 73, 93,
    38, 53, 60, 4, 23]

triangle_test = [
3,
7, 4,
2, 4, 6,
8, 5, 9, 3
]
def main(args):

    if not args:
        tri_data = triangle
    else:
        nums = []
        with open(args[0], 'r') as fp:
            lines = fp.readlines()
            for line in lines:
                line = line.rstrip()
                split_line = line.split(sep=' ')
                nums.extend(split_line)
                pass
        tri_data = [int(tok) for tok in nums]

    tree = NumberTriangle(tri_data)
    tri2 = [-1 for x in tri_data]

    last_pos = len(tri2) - 1
    last_tree_row = tree.row(last_pos)

    cur_top = 0
    tree2 = NumberTriangle(tri2)
    tree.print()
    while True:

        cur_node = tree.node_from_pos(cur_top)
        if cur_node[0] >= 9:
            hook = True

        lb = tree.left_branch(cur_top)

        #print("!!!!!", cur_node, f" top = {cur_top} : lb size = {len(lb)}")
        #print(lb)

        print(f'nd = {cur_node}: pos = {cur_top}')
        if cur_top >= 9:
            hook = True

        for i, c in enumerate(lb):
            pos = c[0]
            tri2[pos] = tri_data[pos]
            parent_nodes = tree.parent_nodes(pos)
            right = parent_nodes[1]
            left = parent_nodes[0]

            if not right and not left:
                continue
            elif right and not left:
                parent_pos = tree.pos_from_node(right)
                tri2[pos] += tri2[parent_pos]
            elif left and not right:
                #print('**********', cur_node)
                parent_pos = tree.pos_from_node(left)
                tri2[pos] += tri2[parent_pos]
            else:
                r_parent_pos = tree.pos_from_node(right)
                l_parent_pos = tree.pos_from_node(left)
                incr = max(tri2[l_parent_pos], tri2[r_parent_pos])
                tri2[pos] += incr

        #tree2.update(tri2)
        #tree2.print()
        if len(lb) == 1:
            break

        next_row = cur_node[0] + 1
        cur_top = tree.start_of_row(next_row + 1) - 1 # end of row


    tree2 = NumberTriangle(tri2)
    tree2.print()
    last_row, _ = tree2.get_row(tree.last_row)
    print(f"max path value = {max(last_row)}")


if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    main(args)