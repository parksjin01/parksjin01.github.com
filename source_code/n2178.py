n, m = map(int, raw_input().strip(" ").split(" "))

canvas = [[0] * (m + 1)]
for _ in range(n):
    canvas.append([0] + map(int, list(raw_input().strip(" "))))

visited = {(1, 1): 1}
history = [(1, 1)]
cur = (1, 1)
cnt = 1

while True:

    try:
        visited[(n, m)]
        break
    except:
        pass

    new_history = []
    # cur = history.pop(0)

    for cur in history:
        try:
            visited[(cur[0] + 1, cur[1])]
        except:
            if cur[0] + 1 <= n and canvas[cur[0] + 1][cur[1]] == 1:
                new_history.append((cur[0] + 1, cur[1]))
                visited[(cur[0] + 1, cur[1])] = 1

        try:
            visited[(cur[0], cur[1] + 1)]
        except:
            if cur[1] + 1 <= m and canvas[cur[0]][cur[1] + 1] == 1:
                new_history.append((cur[0], cur[1] + 1))
                visited[(cur[0], cur[1] + 1)] = 1

        try:
            visited[(cur[0] - 1, cur[1])]
        except:
            if cur[0] - 1 > 0 and canvas[cur[0] - 1][cur[1]] == 1:
                new_history.append((cur[0] - 1, cur[1]))
                visited[(cur[0] - 1, cur[1])] = 1

        try:
            visited[(cur[0], cur[1] - 1)]
        except:
            if cur[1] - 1 > 0 and canvas[cur[0]][cur[1] - 1] == 1:
                new_history.append((cur[0], cur[1] - 1))
                visited[(cur[0], cur[1] - 1)] = 1

    history = new_history[::]

    cnt += 1

print cnt
