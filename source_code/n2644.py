import sys

people = int(sys.stdin.readline())
relation = {}

s, e = map(int, sys.stdin.readline().strip(" ").split(" "))
s -= 1
e -= 1
nr = int(raw_input())

for _ in range(nr):
    ts, te = map(int, sys.stdin.readline().strip(" ").split(" "))
    ts -= 1
    te -= 1
    try:
        relation[ts].append(te)
    except:
        relation[ts] = [te]

    try:
        relation[te].append(ts)
    except:
        relation[te] = [ts]

visited = {s: 1}
bfs = [s]
time = 0

while True:
    try:
        visited[e]
        break
    except:
        pass
    new_bfs = []

    for new_s in bfs:
        for tmp_e in relation[new_s]:
            try:
                visited[tmp_e]
            except:
                visited[tmp_e] = 1
                new_bfs.append(tmp_e)

    bfs = new_bfs[::]
    time += 1

print time
