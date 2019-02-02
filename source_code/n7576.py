import sys

n, m = map(int, sys.stdin.readline().strip(" ").split(" "))

done = {}
bfs = []

tomato = []
answer = []
for _ in range(m):
    tomato.append(map(int, sys.stdin.readline().strip(" ").split(" ")))
    answer.append([1] * n)

for y in range(m):
    for x in range(n):
        if tomato[y][x] == 1:
            done[(y, x)] = 1
            bfs.append((y, x))

        if tomato[y][x] == -1:
            answer[y][x] = -1

prev_tomato = []
time = 0

while True:

    if tomato == answer:
        print time
        break

    new_bfs = []
    change = 0

    for coord in bfs:
        if coord[0] - 1 >= 0 and tomato[coord[0] - 1][coord[1]] == 0:
            done[(coord[0] - 1, coord[1])] = 1
            new_bfs.append((coord[0] - 1, coord[1]))
            tomato[coord[0] - 1][coord[1]] = 1
            change += 1

        if coord[0] + 1 < m and tomato[coord[0] + 1][coord[1]] == 0:
            done[(coord[0] + 1, coord[1])] = 1
            new_bfs.append((coord[0] + 1, coord[1]))
            tomato[coord[0] + 1][coord[1]] = 1
            change += 1

        if coord[1] - 1 >= 0 and tomato[coord[0]][coord[1] - 1] == 0:
            done[(coord[0], coord[1] - 1)] = 1
            new_bfs.append((coord[0], coord[1] - 1))
            tomato[coord[0]][coord[1] - 1] = 1
            change += 1

        if coord[1] + 1 < n and tomato[coord[0]][coord[1] + 1] == 0:
            done[(coord[0], coord[1] + 1)] = 1
            new_bfs.append((coord[0], coord[1] + 1))
            tomato[coord[0]][coord[1] + 1] = 1
            change += 1

    bfs = new_bfs[::]
    time += 1

    if change == 0:
        print -1
        break
