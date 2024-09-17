
import re
import math
canvas_width = 50
def ascii_branch(depth, init, tree = []):
    # TODO this function doesn't quite work!
    # it should draw a tree like the one in tree.txt
    # see if you can fix it
    if depth < 1 :
        return '\n'.join(tree)
    depth = int(depth)
    n_branches = int(init/depth)
    for i in range(1, depth + 1):
        padding = i + depth
        branch = ' ' * padding + '\\' + 2 * (depth -i) * ' ' + '/'
        branch = (branch + ' ' * (i + depth)) * n_branches
        tree.insert(i-1, branch)
    # join horizontally
    return ascii_branch(depth/2, init, tree)
if __name__ == '__main__':
    # draw a v made out of \/
    tree = ascii_branch(8, 8)
    print(tree)


