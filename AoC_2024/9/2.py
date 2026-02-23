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
cnt = 0
st = 0
spaces = [set() for i in range(100)]
for i in range(n):
    if a[i] == '.':
        if i == 0 or a[i - 1] != '.':
            st = i
            cnt = 1
        else:
            cnt += 1
    else:
        if cnt != 0:
            spaces[cnt].add(st)
        cnt = 0

for q in range(100):
    if len(spaces[q]) != 0:
        print(q, end=': ')
        for x in spaces[q]:
            print(x, end=' ')
        print()
print()

j = n - 1
while a[j] == '.':
    j -= 1
while j > -1:
    cnt = 1
    idx = a[j]
    while j > 0 and a[j - 1] == a[j]:
        cnt += 1
        j -= 1

    pos = n + 2
    i_save = -1
    for i in range(cnt, len(spaces)):
        if len(spaces[i]) != 0:
            if min(spaces[i]) < pos:
                pos = min(spaces[i])
                i_save = i

    if pos != n + 2 and pos < j:
        for x in range(cnt):
            a[pos + x] = idx
        for x in range(cnt):
            a[j + x] = '.'
        spaces[i_save].remove(pos)
        if i_save > cnt:
            spaces[i_save - cnt].add(pos + cnt)
    j -= 1
    while a[j] == '.':
        j -= 1

ans = 0
for q in range(n):
    #print(a[q],end='')
    if a[q] != '.':
        ans += q * a[q]
#print()
print(ans)


