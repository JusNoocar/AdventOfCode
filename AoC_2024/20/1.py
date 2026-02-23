n = 141
INF = 1000000000

def Paths(v, cheat, maze, dist, bound, cnt):
    print(f"v: {v}")
    if bound == 0:
        return

    i = v // n
    j = v % n

    offsets = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    for off_i, off_j in offsets:
        if 0 <= i + off_i < n and 0 <= j + off_j < n:
            u = (i + off_i) * n + (j + off_j)
            if maze[i][j] == '#':
                if cheat == 1 and dist[0][u] + 1 == dist[1][v] and dist[1][v] <= bound:
                    Paths(u, 0, maze, dist, bound - 1, cnt)

                if cheat == 2 and dist[1][u] + 1 == dist[2][v] and maze[i + off_i][j + off_j] == '#' and dist[2][v] <= bound:
                    cnt.add((v, u))

            else:
                if cheat == 0 and dist[0][u] + 1 == dist[0][v] and dist[1][v] <= bound:
                    Paths(u, 0, maze, dist, bound - 1, cnt)

                if cheat == 2 and dist[1][u] + 1 == dist[2][v] and maze[i + off_i][j + off_j] == '#' and dist[2][v] <= bound:
                    cnt.add((v, u))

                if cheat == 2 and dist[2][u] + 1 == dist[2][v] and dist[2][v] <= bound:
                    Paths(u, 2, maze, dist, bound - 1, cnt)

def Dijkstra(start, end, maze):
    dist = [[INF] * (n * n) for _ in range(3)]
    dist[0][start] = 0

    que = set()
    que.add((0, start, 0))

    while que:
        v = min(que, key=lambda x: x[0])[1]
        i = v // n
        j = v % n
        cheat = min(que, key=lambda x: x[0])[2]
        que.remove(min(que, key=lambda x: x[0]))
        offsets = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        for off_i, off_j in offsets:
            if 0 <= i + off_i < n and 0 <= j + off_j < n:
                u = (i + off_i) * n + (j + off_j)
                if maze[i + off_i][j + off_j] == '#':
                    if dist[0][v] + 1 < dist[1][u]:
                        que.discard((dist[1][u], u, 1))
                        dist[1][u] = dist[0][v] + 1
                        que.add((dist[1][u], u, 1))

                    if dist[1][v] + 1 < dist[2][u] and maze[i][j] == '#':
                        que.discard((dist[2][u], u, 2))
                        dist[2][u] = dist[1][v] + 1
                        que.add((dist[2][u], u, 2))
                else:
                    if dist[0][v] + 1 < dist[0][u]:
                        que.discard((dist[0][u], u, 0))
                        dist[0][u] = dist[0][v] + 1
                        que.add((dist[0][u], u, 0))

                    if dist[1][v] + 1 < dist[2][u] and maze[i][j] == '#':
                        que.discard((dist[2][u], u, 2))
                        dist[2][u] = dist[1][v] + 1
                        que.add((dist[2][u], u, 2))

                    if dist[2][v] + 1 < dist[2][u]:
                        que.discard((dist[2][u], u, 2))
                        dist[2][u] = dist[2][v] + 1
                        que.add((dist[2][u], u, 2))

    ans = INF
    for i in range(3):
        ans = min(ans, dist[i][end])

    for i in range(n):
        for j in range(n):
            k = INF
            v = i * n + j
            for q in range(3):
                k = min(k, dist[q][v])
            if k == INF:
                print(maze[i][j], end='')
            elif dist[0][v] != INF:
                print('@', end='')
            else:
                print(maze[i][j], end='')
        print()

    bound = 84
    cnt = set()
    Paths(end, 1, maze, dist, bound, cnt)
    Paths(end, 2, maze, dist, bound, cnt)
    print(len(cnt))

    return ans

def Dijkstra_norm(start, end, maze):
    dist = [INF] * (n * n)
    dist[start] = 0

    que = set()
    que.add((0, start))

    while que:
        v = min(que, key=lambda x: x[0])[1]
        i = v // n
        j = v % n
        que.remove(min(que, key=lambda x: x[0]))
        offsets = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        for off_i, off_j in offsets:
            if 0 <= i + off_i < n and 0 <= j + off_j < n:
                u = (i + off_i) * n + (j + off_j)
                if maze[i + off_i][j + off_j] != '#':
                    if dist[v] + 1 < dist[u]:
                        que.discard((dist[u], u))
                        dist[u] = dist[v] + 1
                        que.add((dist[u], u))

    ans = INF
    ans = min(ans, dist[end])

    return ans

def main():
    with open("test.txt", "r") as f:
        maze = [list(f.readline().strip()) for _ in range(n)]

    start = end = 0

    for i in range(n):
        for j in range(n):
            if maze[i][j] == 'E':
                end = i * n + j
            elif maze[i][j] == 'S':
                start = i * n + j

    print(start, end)

    cnt = 0
    mx_ans = Dijkstra_norm(start, end, maze)
    bound = mx_ans - 100
    for i in range(n):
        for j in range(n):
            if maze[i][j] != '#':
                continue
            offsets = [(-1, 0), (0, -1), (1, 0), (0, 1)]
            for off_i, off_j in offsets:
                if 0 <= i + off_i < n and 0 <= j + off_j < n:
                    save = maze[i + off_i][j + off_j]
                    maze[i][j] = '.'
                    maze[i + off_i][j + off_j] = '.'
                    if Dijkstra_norm(start, end, maze) <= bound:
                        cnt += 1
                    maze[i][j] = '#'
                    maze[i + off_i][j + off_j] = save

    print(cnt)

main()