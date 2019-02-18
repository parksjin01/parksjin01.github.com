import sys
import copy

x, y, layer = map(int, sys.stdin.readline().strip(" ").split(" "))

done = {}
bfs = []

tomato_stack = []
answer_stack = []
for _ in range(layer):
    answer = []
    tomato = []
    for _ in range(y):
        tomato.append(map(int, sys.stdin.readline().strip(" ").split(" ")))
        answer.append([1] * x)
    tomato_stack.append(copy.deepcopy(tomato))
    answer_stack.append(copy.deepcopy(answer))

for cur_layer in range(layer):
    for cur_y in range(y):
        for cur_x in range(x):
            if tomato_stack[cur_layer][cur_y][cur_x] == 1:
                done[(cur_layer, cur_y, cur_x)] = 1
                bfs.append((cur_layer, cur_y, cur_x))

            if tomato_stack[cur_layer][cur_y][cur_x] == -1:
                answer_stack[cur_layer][cur_y][cur_x] = -1

prev_tomato = []
time = 0

# print answer_stack

while True:
    if tomato_stack == answer_stack:
        print time
        break

    new_bfs = []
    change = 0

    for coord in bfs:
        if coord[0] - 1 >= 0 and tomato_stack[coord[0] - 1][coord[1]][coord[2]] == 0:
            done[(coord[0] - 1, coord[1], coord[2])] = 1
            new_bfs.append((coord[0] - 1, coord[1], coord[2]))
            tomato_stack[coord[0] - 1][coord[1]][coord[2]] = 1
            change += 1

        if coord[0] + 1 < layer and tomato_stack[coord[0] + 1][coord[1]][coord[2]] == 0:
            done[(coord[0] + 1, coord[1], coord[2])] = 1
            new_bfs.append((coord[0] + 1, coord[1], coord[2]))
            tomato_stack[coord[0] + 1][coord[1]][coord[2]] = 1
            change += 1

        if coord[1] - 1 >= 0 and tomato_stack[coord[0]][coord[1] - 1][coord[2]] == 0:
            done[(coord[0], coord[1] - 1, coord[2])] = 1
            new_bfs.append((coord[0], coord[1] - 1, coord[2]))
            tomato_stack[coord[0]][coord[1] - 1][coord[2]] = 1
            change += 1

        if coord[1] + 1 < y and tomato_stack[coord[0]][coord[1] + 1][coord[2]] == 0:
            done[(coord[0], coord[1] + 1, coord[2])] = 1
            new_bfs.append((coord[0], coord[1] + 1, coord[2]))
            tomato_stack[coord[0]][coord[1] + 1][coord[2]] = 1
            change += 1

        if coord[2] - 1 >= 0 and tomato_stack[coord[0]][coord[1]][coord[2] - 1] == 0:
            done[(coord[0], coord[1], coord[2] - 1)] = 1
            new_bfs.append((coord[0], coord[1], coord[2] - 1))
            tomato_stack[coord[0]][coord[1]][coord[2] - 1] = 1
            change += 1

        if coord[2] + 1 < x and tomato_stack[coord[0]][coord[1]][coord[2] + 1] == 0:
            done[(coord[0], coord[1], coord[2] + 1)] = 1
            new_bfs.append((coord[0], coord[1], coord[2] + 1))
            tomato_stack[coord[0]][coord[1]][coord[2] + 1] = 1
            change += 1

    bfs = new_bfs[::]
    time += 1

    if change == 0:
        print -1
        break
