tc = int(raw_input())

for _ in range(tc):
    apt = []
    apt_coord = {}
    visited = {}

    m, n, k = map(int, raw_input().strip(" ").split(" "))
    template = [0] * m
    for _ in range(n):
        apt.append(template[::])

    for _ in range(k):
        x, y = map(int, raw_input().strip(" ").split(" "))
        apt[y][x] = 1

    for y in range(n):
        for x in range(m):
            if apt[y][x] == 1:
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
                            if coord[0] - 1 >= 0 and apt[coord[0] - 1][coord[1]] == 1:
                                new_bfs.append((coord[0] - 1, coord[1]))
                                apt_comp.append((coord[0] - 1, coord[1]))
                                visited[(coord[0] - 1, coord[1])] = 1
                                change += 1

                        try:
                            visited[(coord[0] + 1, coord[1])]
                            # continue
                        except:
                            if coord[0] + 1 < n and apt[coord[0] + 1][coord[1]] == 1:
                                new_bfs.append((coord[0] + 1, coord[1]))
                                apt_comp.append((coord[0] + 1, coord[1]))
                                visited[(coord[0] + 1, coord[1])] = 1
                                change += 1

                        try:
                            visited[(coord[0], coord[1] - 1)]
                            # continue
                        except:
                            if coord[1] - 1 >= 0 and apt[coord[0]][coord[1] - 1] == 1:
                                new_bfs.append((coord[0], coord[1] - 1))
                                apt_comp.append((coord[0], coord[1] - 1))
                                visited[(coord[0], coord[1] - 1)] = 1
                                change += 1

                        try:
                            visited[(coord[0], coord[1] + 1)]
                            # continue
                        except:
                            if coord[1] + 1 < m and apt[coord[0]][coord[1] + 1] == 1:
                                new_bfs.append((coord[0], coord[1] + 1))
                                apt_comp.append((coord[0], coord[1] + 1))
                                visited[(coord[0], coord[1] + 1)] = 1
                                change += 1

                    bfs = new_bfs[::]
                    if change == 0:
                        apt_coord[(y, x)] = apt_comp
                        break




    # print apt_coord

    print len(apt_coord.keys())
