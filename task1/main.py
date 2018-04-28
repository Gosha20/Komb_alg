from _collections import deque

count_v = 0
graph = {}
main_deque = deque()
t = 0
comps = []


def write_file():
    with open('out.txt', 'w', encoding='utf-8') as file:
        count_comp = len(comps)
        file.write(str(count_comp)+'\n')
        print()
        for i in range(count_comp):
            for v in sorted(comps[i]):
                file.write(str(v))
            if i + 1 == count_comp:
                file.write('0')
            else:
                file.write('0\n')


def read_file():
    v = 0
    global graph
    global count_v
    with open('in.txt','r', encoding='utf-8') as file:
        for line in file:
            line = line.rstrip("\n")
            if v > 0:
                graph[v] = [int(x) for x in list(line[:-1])]
            else:
                count_v = int(line)
                graph = {x: 0 for x in range(1, count_v + 1)}
            v += 1


def bfs(s):
    global t

    main_deque.append(s)
    if levels[s] is -1:
        comps[t].append(s)
    levels[s] = 0
    while main_deque:
        v = main_deque.popleft()

        # if levels[v] is -1:
        #     comps[t].append(v)
        # levels[s] = 0
        for w in graph[v]:
            if levels[w] is -1:
                main_deque.append(w)
                comps[t].append(w)
                levels[w] = levels[v] + 1
    t += 1

read_file()
levels = [-1 for x in range(count_v + 1)]
for i in graph.keys():
    if levels[i] is -1:
        comps.append([])
        bfs(i)
write_file()