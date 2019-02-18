def counting(color, n):
    visited = {}
    cnt = 0

    for y in range(n):
        for x in range(n):
            try:
                visited[(y, x)]
                continue
            except:
                pass
            visited[(y, x)] = 1
            # tmp_res = []
            bfs = [(y, x)]
            cnt += 1

            while len(bfs) > 0:
                new_bfs = []

                for coord in bfs:
                    try:
                        visited[(coord[0] - 1, coord[1])]
                    except:
                        if coord[0] - 1 >= 0 and color[coord[0] - 1][coord[1]] == color[y][x]:
                            visited[(coord[0] - 1, coord[1])] = 1
                            new_bfs.append((coord[0] - 1, coord[1]))

                    try:
                        visited[(coord[0] + 1, coord[1])]
                    except:
                        if coord[0] + 1 < n and color[coord[0] + 1][coord[1]] == color[y][x]:
                            visited[(coord[0] + 1, coord[1])] = 1
                            new_bfs.append((coord[0] + 1, coord[1]))

                    try:
                        visited[(coord[0], coord[1] - 1)]
                    except:
                        if coord[1] - 1 >= 0 and color[coord[0]][coord[1] - 1] == color[y][x]:
                            visited[(coord[0], coord[1] - 1)] = 1
                            new_bfs.append((coord[0], coord[1] - 1))

                    try:
                        visited[(coord[0], coord[1] + 1)]
                    except:
                        if coord[1] + 1 < n and color[coord[0]][coord[1] + 1] == color[y][x]:
                            visited[(coord[0], coord[1] + 1)] = 1
                            new_bfs.append((coord[0], coord[1] + 1))

                # tmp_res += bfs
                bfs = new_bfs[::]
            # print tmp_res
    return cnt

num = int(raw_input().strip(" "))
normal_color = []
rg_color = []

for _ in range(num):
    normal_color.append(list(raw_input().strip(" ")))
    tmp = []
    for c in normal_color[-1]:
        if c != 'G':
            tmp.append(c)
        else:
            tmp.append('R')
    rg_color.append(tmp)

print counting(normal_color, num), counting(rg_color, num)
