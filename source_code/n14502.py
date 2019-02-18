import pprint
import copy

def count(canvas, height, width):
    cnt = 0
    for y in range(height):
        for x in range(width):
            if canvas[y][x] == 0:
                cnt += 1

    return cnt

def bfs_search(canvas, bfs, height, width):
    while True:
        change = False
        new_bfs = []

        for coord in bfs:
            # pprint.pprint(canvas, width=100)
            # try:
            #     history[(coord[0] - 1, coord[1])]
            # except:
            if coord[0] - 1 >= 0 and canvas[coord[0] - 1][coord[1]] == 0:
                canvas[coord[0] - 1][coord[1]] = 2
                new_bfs.append([coord[0] - 1, coord[1]])
                change = True

            # try:
            #     history[(coord[0] + 1, coord[1])]
            # except:
            if coord[0] + 1 < height and canvas[coord[0] + 1][coord[1]] == 0:
                canvas[coord[0] + 1][coord[1]] = 2
                new_bfs.append([coord[0] + 1, coord[1]])
                change = True

            # try:
            #     history[(coord[0], coord[1] - 1)]
            # except:
            if coord[1] - 1 >= 0 and canvas[coord[0]][coord[1] - 1] == 0:
                canvas[coord[0]][coord[1] - 1] = 2
                new_bfs.append([coord[0], coord[1] - 1])
                change = True

            # try:
            #     history[(coord[0], coord[1] + 1)]
            # except:
            if coord[1] + 1 < width and canvas[coord[0]][coord[1] + 1] == 0:
                canvas[coord[0]][coord[1] + 1] = 2
                new_bfs.append([coord[0], coord[1] + 1])
                change = True

        if not change:
            break

        bfs = new_bfs[::]

    return count(canvas, height, width)

def full_search(canvas, bfs, available, height, width):
    length = len(available)
    res = 0

    for i in range(length):
        for j in range(i + 1, length):
            for k in range(j + 1, length):
                new_canvas = copy.deepcopy(canvas)
                new_canvas[available[i][0]][available[i][1]] = 1
                new_canvas[available[j][0]][available[j][1]] = 1
                new_canvas[available[k][0]][available[k][1]] = 1

                res = max(res, bfs_search(new_canvas, bfs[::], height, width))

    return res

height, width = map(int, raw_input().strip(" ").split(" "))

canvas = []
bfs = []
available = []

for y in range(height):
    canvas.append(map(int, raw_input().strip(" ").split(" ")))
    for idx in range(width):
        if canvas[y][idx] == 2:
            bfs.append([y, idx])

        if canvas[y][idx] == 0:
            available.append([y, idx])

print full_search(canvas, bfs[::], available, height, width)
