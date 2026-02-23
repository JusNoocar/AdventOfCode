f = open('test.txt')
data = f.readlines()
a = [[] for i in range(len(data))]
for i in range(len(data)):
    data[i] = data[i].strip()
    k = len(data[i])
    for j in range(k):
        a[i].append(data[i][j])

print(len(a))
print(len(a[0]))
print(a[0])
n = len(a)
m = len(a[0])
cnt = 0
print(a[9][9])
for i in range(n):
    for j in range(m):
        if j >= 3:
            s = a[i][j - 3] + a[i][j - 2] + a[i][j - 1] + a[i][j]
            if s == "XMAS" or s == "SAMX":
                cnt += 1

        if i >= 3:
            s = a[i - 3][j] + a[i - 2][j] + a[i - 1][j] + a[i][j]
            if s == "XMAS" or s == "SAMX":
                cnt += 1
        if j >= 3 and i >= 3:
            s = a[i - 3][j - 3] + a[i - 2][j - 2] + a[i - 1][j - 1] + a[i][j]
            if s == "XMAS" or s == "SAMX":
                cnt += 1

        if j >= 3 and i < n - 3:
            s = a[i + 3][j - 3] + a[i + 2][j - 2] + a[i + 1][j - 1] + a[i][j]
            if s == "XMAS" or s == "SAMX":
                cnt += 1


print(cnt)