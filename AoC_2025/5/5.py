with open("5.txt") as f:
    line = f.readline().strip()
    fresh = []
    while line != "":
        fresh.append(list(map(int, line.split("-"))))
        line = f.readline().strip()

cnt = 0
fresh.sort(key=lambda x: [x[0], -x[1]])
print(fresh)
i = 0
for [l, r] in fresh:
    i = max(i, l)
    if r - i >= 0:
        cnt += (r - i + 1)
    i = max(i, r + 1)
print(cnt)