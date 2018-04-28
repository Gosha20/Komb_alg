import sys

count_lifers = int(input())
child_parent = {x: [] for x in range(1, count_lifers + 1)}
parent_children = {x: [] for x in range(1, count_lifers + 1)}
answer = [1 for x in range(1, count_lifers+1)]
dead = []
blood = 0
for line in sys.stdin:
    line = line.rstrip('\n')
    if line == "":
        break
    if line == "BLOOD":
        blood = 1
        continue
    if blood == 0:
        children, parent = line.split()
        child_parent[int(children)].append(int(parent))
        parent_children[int(parent)].append(int(children))
    else:
        dead.append(int(line))


def skip(man):
    skip_parent(man)
    skip_children(man)


def skip_parent(man):
    for i in child_parent[man]:
        if i != 0 and i in child_parent:
            skip_parent(i)
    answer[man-1] = 0
    # child_parent.pop(man)


def skip_children(man):
    for i in parent_children[man]:
        if i != 0 and i in parent_children:
            skip_children(i)
    answer[man - 1] = 0


for i in dead:
    skip(i)
result = []

def find_answer():
    for k in range(1, count_lifers+1):
        if answer[k-1] == 1:
            result.append(str(k))


find_answer()
if len(result) == 0:
    print("0")
else:
    print(" ".join(result))
