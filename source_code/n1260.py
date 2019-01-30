import sys
sys.setrecursionlimit(100000)

node, edge, start = map(int, raw_input().strip(" ").split(" "))
template = [0] * (node + 1)
graph = []

def dfs(graph, start, visited):
    for idx in range(len(graph[start])):
        if graph[start][idx] == 1 and idx not in visited:
            visited.append(idx)
            dfs(graph, idx, visited)

    return visited

for _ in range(node + 1):
    graph.append(template[::])

for _ in range(edge):
    s, e = map(int, raw_input().strip(" ").split(" "))
    graph[s][e] = 1
    graph[e][s] = 1

visited = [start]
dfs(graph, start, visited)
print " ".join(map(str, visited))

visited = [start]
bfs = [start]

while len(visited) < node:
    try:
        start = bfs.pop(0)
        for idx in range(len(graph[start])):
            if graph[start][idx] == 1 and idx not in visited:
                visited.append(idx)
                bfs.append(idx)
    except:
        break

print " ".join(map(str, visited))
