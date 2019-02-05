def print_canvas(canvas):
    print "\n".join(" ".join(map(str, line)) for line in canvas)

size = int(raw_input().strip(" "))
template = [0] * size
canvas = []
edge = []
path = {}

for y in range(size):
    tmp = map(int, raw_input().strip(" ").split(" "))
    canvas.append(template[::])
    for x in range(len(tmp)):
        if tmp[x] == 1:
            edge.append([y, x])

for y in range(size):
    bfs = [y]
    visited = {}
    p = []

    while True:
        new_bfs = []
        change = 0

        for cur in bfs:
            for e in edge:
                if e[0] == cur:
                    try:
                        visited[e[1]]
                    except:
                        visited[e[1]] = 1
                        new_bfs.append(e[1])
                        p.append(e[1])
                        change = 1

        if change == 0:
            break

        bfs = new_bfs[::]

    path[y] = p

for y in range(size):
    for x in path[y]:
        canvas[y][x] = 1

print_canvas(canvas)
