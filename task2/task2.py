import copy
import sys

count_lines = 0
count_columns = 0
labyrinth = []
point_from = (0, 0)
point_to = (0, 0)


def read_file():
    global count_lines
    global count_columns
    global point_from
    global point_to
    with open('in.txt', 'r', encoding='utf-8') as file:
        count_lines = int(file.readline().rstrip("\n"))
        count_columns = int(file.readline().rstrip("\n"))
        for i in range(count_lines):
            labyrinth.append(list(file.readline().rstrip("\n").replace(" ", "")))

        x, y = file.readline().rstrip('\n').split(" ")
        point_from = (int(x) - 1, int(y) - 1)
        x, y = file.readline().rstrip('\n').split(" ")
        point_to = (int(x) - 1, int(y) - 1)


def write_file(path):
    with open('out.txt', 'w', encoding='utf-8') as file:
        file.write("Y\n")
        for i in path:
            x = i[0]+1
            y = i[1]+1
            file.write(str(x)+" "+str(y)+"\n")


def dfs(node, path):  # start - начальная вершина
    path.append(node)
    labyrinth[node[0]][node[1]] = 'x'
    if node == point_to:
        write_file(path)
        sys.exit(0)

    for dx in [0, -1, 1]:
        for dy in [0, -1, 1]:
            if abs(dx * dy) != 1 and not dy == dx == 0:
                if (node[0] + dx < len(labyrinth)) \
                        and (node[1] + dy < len(labyrinth[0])) \
                        and labyrinth[node[0] + dx][node[1] + dy] == '0':
                    a = copy.deepcopy(path)
                    dfs((node[0] + dx, node[1] + dy), a)
	

def print1():
    for line in labyrinth:
        print(line)
    print()


read_file()
dfs(point_from, [])
with open('out.txt', 'w', encoding='utf-8') as file:
    file.write("N")
# dfs(point_from)
# print(count_lines, count_columns)
# print(point_from)
# print(point_to)
