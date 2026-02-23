f = open('test.txt')
a = list(map(int, f.read().strip().split(' ')))
for q in range(75):
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

print(len(a))