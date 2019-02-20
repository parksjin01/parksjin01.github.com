import sys

def bacon(graph, node):
    bfs = [node]
    visited = {node: 1}
    res = 0
    inc = 1

    while True:
        change = False
        new_bfs = []

        for n in bfs:
            for cur_node in graph[n]:
                try:
                    visited[cur_node]
                except:
                    visited[cur_node] = 1
                    res += inc
                    new_bfs.append(cur_node)
                    change = True

        if not change:
            break

        bfs = new_bfs[::]
        inc += 1

    return res


node, connection = map(int, raw_input().strip(" ").split(" "))
graph = {}

for _ in range(connection):
    n1, n2 = map(int, raw_input().strip(" ").split(" "))

    try:
        graph[n1].append(n2)
    except:
        graph[n1] = [n2]

    try:
        graph[n2].append(n1)
    except:
        graph[n2] = [n1]

value = sys.maxint
min_node = 0
for cur_node in range(1, node + 1):
    node_bacon = bacon(graph, cur_node)
    if node_bacon < value:
        min_node = cur_node
        value = node_bacon

print min_node
