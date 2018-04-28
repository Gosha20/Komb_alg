import copy
import sys
import copy

n = 0
point_from = 0
point_to = 0
matrix = []


def read_file():
    global n
    global point_from
    global point_to
    with open('in.txt', 'r', encoding='utf-8') as file:
        n = int(file.readline().rstrip("\n"))
        for i in range(n):
            matrix.append([int(x) for x in file.readline().rstrip('\n').split()])
        point_from = int(file.readline().rstrip('\n')) - 1
        point_to = int(file.readline().rstrip('\n')) - 1


def write_file(path,max_weight):
    with open('out.txt', 'w', encoding='utf-8') as file:
        if len(result_path) is not 0:
            file.write("Y\n")
            result = ''
            for i in path:
                result += str(i)+ " "
            file.write(result.rstrip() + '\n')
            file.write(str(max_weight))
        else:
            file.write('N')


def dijkstra(N, S, matrix):
    valid = [True] * N
    weight = [1000000] * N
    weight[S] = 0
    for i in range(N):
        min_weight = 1000001
        ID_min_weight = -1
        # ыбирается минимальная метка вершины из не посещенных
        for i in range(N):
            if valid[i] and weight[i] < min_weight:
                min_weight = weight[i]
                ID_min_weight = i
        for i in range(N):
            if matrix[ID_min_weight][i] != -32768:
                if weight[ID_min_weight] + matrix[ID_min_weight][i] < weight[i]:
                    weight[i] = weight[ID_min_weight] + matrix[ID_min_weight][i]
            valid[ID_min_weight] = False
    return weight


def find_path(point_from, point_to, matrix, weight):
    path = []
    point_to = point_to
    path.append(point_to)
    while weight[point_to] < 1000000:
        for j in range(len(weight)):
            if matrix[j][point_to] != -32768:
                if weight[point_to] - matrix[j][point_to] == weight[j]:
                    path.append(j)
                    point_to = j
                    break
        if point_from == point_to:
            break
    if len(path) != 1:
        path = path[::-1]
        max_w = max([matrix[path[x]][path[x+1]] for x in range(len(path)-1)])
        return [x+1 for x in path], max_w
    return [], 0

read_file()
w = dijkstra(n, point_from, matrix)
result_path, max_w = find_path(point_from, point_to, matrix, w)
write_file(result_path, max_w)

