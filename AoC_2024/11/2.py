f = open('test.txt')
a = list(map(int, f.read().strip().split(' ')))
data = [[0 for j in range(1000001)] for i in range(51)]
for j in range(1000001):
    data[0][j] = 1
for i in range(1, 51):
    for j in range(1000001):
        if j == 0:
            data[i][j] = data[i - 1][1]
        elif len(str(j)) % 2 == 0:
            m = len(str(j)) // 2
            k1 = int(str(j)[:m])
            k2 = int(str(j)[m:])
            data[i][j] = data[i - 1][k1] + data[i - 1][k2]
        elif j * 2024 < 1000001:
            data[i][j] = data[i - 1][j * 2024]
        elif i == 1:
            data[i][j] = 1
        else:
            j1 = j
            cnt = 1
            while len(str(j1)) % 2 != 0:
                j1 *= 2024
                cnt += 1
            m = len(str(j1)) // 2
            k1 = int(str(j1)[:m])
            k2 = int(str(j1)[m:])
            if i - cnt >= 0:
                data[i][j] = data[i - cnt][k1] + data[i - cnt][k2]
            else:
                data[i][j] = 1

for q in range(25):
    b = []
    for i in range(len(a)):
        if a[i] == 0:
            b.append(1)
        elif len(str(a[i])) % 2 == 0:
            m = len(str(a[i])) // 2
            k1 = int(str(a[i])[:m])
            k2 = int(str(a[i])[m:])
            b.append(k1)
            b.append(k2)
        else:
            b.append(a[i] * 2024)

    a = b
print(a)
ans = 0
for x in a:
    if len(str(x)) % 2 == 0:
        m = len(str(x)) // 2
        k1 = int(str(x)[:m])
        k2 = int(str(x)[m:])

        if len(str(k1)) % 2 == 0:
            m1 = len(str(k1)) // 2
            k3 = int(str(k1)[:m1])
            k4 = int(str(k1)[m1:])
            ans += data[48][k3] + data[48][k4]
        else:
            ans += data[49][k1]

        if len(str(k2)) % 2 == 0:
            m1 = len(str(k2)) // 2
            k3 = int(str(k2)[:m1])
            k4 = int(str(k2)[m1:])
            ans += data[48][k3] + data[48][k4]
        else:
            ans += data[49][k2]

    else:
        if x > 100000:
            cnt = 1
            while len(str(x)) % 2 != 0:
                x *= 2024
                cnt += 1
            m = len(str(x)) // 2
            k1 = int(str(x)[:m])
            k2 = int(str(x)[m:])
            ans += data[50 - cnt][k1] + data[50 - cnt][k2]
        else:
            ans += data[50][x]
print(ans)