f = open('test.txt')
inp = list(map(int, f.read().strip().split(' ')))
a = dict()
for x in inp:
    if x not in a:
        a[x] = 1
    else:
        a[x] += 1
for q in range(75):
    b = dict()
    for key in a:
        if key == 0:
            if 1 not in b:
                b[1] = 0
            b[1] += a[key]
        elif len(str(key)) % 2 == 0:
            m = len(str(key)) // 2
            k1 = int(str(key)[:m])
            k2 = int(str(key)[m:])
            if k1 not in b:
                b[k1] = 0
            if k2 not in b:
                b[k2] = 0
            b[k1] += a[key]
            b[k2] += a[key]
        else:
            if key * 2024 not in b:
                b[key * 2024] = 0
            b[key * 2024] += a[key]

    a = b

ans = 0
for key in a:
    ans += a[key]
print(ans)