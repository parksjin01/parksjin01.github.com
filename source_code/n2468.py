import sys

n= int(sys.stdin.readline())

apt = []
# apt_coord = {}
# visited = {}
minimum = 987654321
maximum = 0
res = []

for _ in range(n):
    apt.append(map(int, sys.stdin.readline().strip(" ").split(" ")))
    minimum = min(minimum, min(apt[-1]))
    maximum = max(maximum, max(apt[-1]))

for limit in range(0, maximum + 1):

    apt_coord = {}
    visited = {}

    for y in range(n):
        for x in range(n):

            if apt[y][x] >= limit:
                try:
                    visited[(y, x)]
                    continue
                except:
                    visited[(y, x)] = 1
                    pass

                bfs = [(y, x)]
                apt_comp = [(y, x)]
                while True:
                    new_bfs = []
                    change = 0
                    for coord in bfs:
                        try:
                            visited[(coord[0] - 1, coord[1])]
                            # continue
                        except:
                            if coord[0] - 1 >= 0 and apt[coord[0] - 1][coord[1]] >= limit:
                                new_bfs.append((coord[0] - 1, coord[1]))
                                apt_comp.append((coord[0] - 1, coord[1]))
                                visited[(coord[0] - 1, coord[1])] = 1
                                change += 1

                        try:
                            visited[(coord[0] + 1, coord[1])]
                            # continue
                        except:
                            if coord[0] + 1 < n and apt[coord[0] + 1][coord[1]] >= limit:
                                new_bfs.append((coord[0] + 1, coord[1]))
                                apt_comp.append((coord[0] + 1, coord[1]))
                                visited[(coord[0] + 1, coord[1])] = 1
                                change += 1

                        try:
                            visited[(coord[0], coord[1] - 1)]
                            # continue
                        except:
                            if coord[1] - 1 >= 0 and apt[coord[0]][coord[1] - 1] >= limit:
                                new_bfs.append((coord[0], coord[1] - 1))
                                apt_comp.append((coord[0], coord[1] - 1))
                                visited[(coord[0], coord[1] - 1)] = 1
                                change += 1

                        try:
                            visited[(coord[0], coord[1] + 1)]
                            # continue
                        except:
                            if coord[1] + 1 < n and apt[coord[0]][coord[1] + 1] >= limit:
                                new_bfs.append((coord[0], coord[1] + 1))
                                apt_comp.append((coord[0], coord[1] + 1))
                                visited[(coord[0], coord[1] + 1)] = 1
                                change += 1

                    bfs = new_bfs[::]
                    if change == 0:
                        apt_coord[(y, x)] = apt_comp
                        break


    res.append(len(apt_coord.keys()))

print max(res)
