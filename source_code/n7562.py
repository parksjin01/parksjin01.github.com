moving = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

tc = int(raw_input().strip(" "))
for _ in range(tc):
    size = int(raw_input().strip(" "))
    cur = tuple(map(int, raw_input().strip(" ").split(" ")))
    target = tuple(map(int, raw_input().strip(" ").split(" ")))
    visited = {cur: 1}
    bfs = [cur]
    time = 0

    while True:
        if tuple(target) in visited:
            break
        # print time, visited
        new_bfs = []
        for cur in bfs:
            for m in moving:
                tmp_cur = (cur[0] - m[0], cur[1] - m[1])
                try:
                    visited[tmp_cur]
                except:
                    if 0 <= tmp_cur[0] and tmp_cur[0] < size and 0 <= tmp_cur[1] and tmp_cur[1] < size:
                        visited[tmp_cur] = 1
                        new_bfs.append(tmp_cur)

        bfs = new_bfs[::]

        time += 1

    print time
