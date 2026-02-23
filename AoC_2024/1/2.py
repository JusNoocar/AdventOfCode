f = open('test.txt')
data = f.readlines()
a = list()
b = list()
for line in data:
    x, y = map(int, line.split())
    a.append(x)
    b.append(y)

a.sort()
b.sort()
ans = 0
for i in range(len(a)):
    print(b.count(a[i]))
    ans += a[i] * b.count(a[i])

print(ans)