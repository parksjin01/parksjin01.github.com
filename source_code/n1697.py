n, m = map(int, raw_input().strip(" ").split(" "))

visited = {n: 1}
bfs = [n]
time = 0

while True:

    try:
        visited[m]
        print time
        break
    except:
        pass

    new_bfs = []

    for cur in bfs:
        try:
            visited[cur - 1]
        except:
            if cur - 1 >= 0:
                visited[cur - 1] = 1
                new_bfs.append(cur - 1)

        try:
            visited[cur + 1]
        except:
            if cur + 1 <= m:
                visited[cur + 1] = 1
                new_bfs.append(cur + 1)

        try:
            visited[2 * cur]
        except:
            if abs(m - cur) >= abs(m - 2 * cur):
                visited[2 * cur] = 1
                new_bfs.append(2 * cur)

    time += 1
    bfs = new_bfs[::]
