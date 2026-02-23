with open("9.txt") as f:
    a = [list(map(int, line.strip().split(','))) for line in f.readlines()]

ans = 0
n = len(a)
for i in range(n):
    for j in range(i + 1, n):
        cnt = abs(a[i][0] - a[j][0] + 1) * abs(a[i][1] - a[j][1] + 1)
        ans = max(ans, cnt)

print(ans)