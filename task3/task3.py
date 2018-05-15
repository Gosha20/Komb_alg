
n = 0
point_from = 0
point_to = 0
matrix = []


def read_file():
    global n
    global point_from
    global point_to
    with open('in2.txt', 'r', encoding='utf-8') as file:
        n = int(file.readline().rstrip("\n"))
        for i in range(n):
            matrix.append([int(x) for x in file.readline().rstrip('\n').split()])
        point_from = int(file.readline().rstrip('\n')) - 1
        point_to = int(file.readline().rstrip('\n')) - 1


def write_file(_path, max_weight):
    with open('out.txt', 'w', encoding='utf-8') as file:
        if len(_path) is not 0:
            file.write("Y\n")
            result = ''
            for i in _path:
                result += str(i+1)+ " "
            file.write(result.rstrip() + '\n')
            file.write(str(max_weight))
        else:
            file.write('N')


def dijkstra(N, S, matrix):
    valid = [True] * N
    weight = [1000000] * N
    weight[S] = 0
    parent = [S]*(N)
    parent[S] = -1
    for i in range(N):
        min_weight = 1000001
        ID_min_weight = -1
        # бирается мин метка вершины из не посещенных
        for i in range(N):
            if valid[i] and weight[i] < min_weight:
                min_weight = weight[i]
                ID_min_weight = i
        for i in range(N):
            if matrix[ID_min_weight][i] != -32768:
                if weight[i] > max(weight[ID_min_weight], matrix[ID_min_weight][i]):
                    weight[i] = max(weight[ID_min_weight], matrix[ID_min_weight][i])
                    parent[i] = ID_min_weight
            valid[ID_min_weight] = False
    return weight, [x for x in parent]



def find_path(point_from, point_to, parents):
    path = []
    point_to = point_to
    if parents[point_to] < 1000000:
        path.append(point_to)
        v = point_to
        while v != point_from:
            w = parents[v]
            path.append(w)
            v = w
        path = path[::-1]
        return path
    return []



read_file()
w, perents = dijkstra(n, point_from, matrix)
path = find_path(point_from, point_to, perents)
write_file(path, w[point_to])