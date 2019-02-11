import sys

num_node, num_edge = map(int, sys.stdin.readline().strip("\n").strip(" ").split(" "))
edge = {}
path = {}
visited_node = {}
idx = 0

while idx < num_edge:
    y, x = map(int, sys.stdin.readline().strip("\n").strip(" ").split(" "))
    try:
        edge[y - 1].append(x - 1)
    except:
        edge[y - 1] = [x - 1]
    try:
        edge[x - 1].append(y - 1)
    except:
        edge[x - 1] = [y - 1]
    idx += 1

for y in range(num_node):
    bfs = [y]
    visited = {}
    p = []
    try:
        visited_node[y]
        continue
    except:
        pass

    try:
        while True:
            new_bfs = []
            change = 0

            for cur in bfs:
                for e in edge[cur]:
                    try:
                        visited[e]
                    except:
                        visited[e] = 1
                        visited_node[e] = 1
                        new_bfs.append(e)
                        p.append(e)
                        change = 1

            if change == 0:
                break

            bfs = new_bfs[::]
    except:
        p = [y]

    if p != []:
        path[y] = p

# for y in range(size):
#     for x in path[y]:
#         canvas[y][x] = 1
#
# print_canvas(canvas)

print len(path)
