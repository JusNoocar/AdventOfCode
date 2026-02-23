f = open('test.txt')
data = f.read().strip()
a = []
idx = 0
for i in range(len(data)):
    if i % 2 == 0:
        for j in range(int(data[i])):
            a.append(idx)
        idx += 1
    else:
        for j in range(int(data[i])):
            a.append('.')

n = len(a)
i = 0
j = n - 1
while a[i] != '.':
    i += 1
while a[j] == '.':
    j -= 1
while i < n and j > -1 and i <= j:
    a[i] = a[j]
    a[j] = '.'
    while a[i] != '.':
        i += 1
    while a[j] == '.':
        j -= 1

ans = 0
for q in range(n):
    if a[q] != '.':
        ans += q * a[q]
print(ans)


