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
        if j >= 2 and i >= 2:
            s1 = a[i - 2][j - 2] + a[i - 1][j - 1] + a[i][j]
            s2 = a[i][j - 2] + a[i - 1][j - 1] + a[i - 2][j]
            if (s1 == "MAS" or s1 == "SAM") and (s2 == "MAS" or s2 == "SAM"):
                cnt += 1



print(cnt)