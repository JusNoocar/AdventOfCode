f = open('test.txt')
data = f.readlines()
cnt = 0
idx = 0
unmarked = list()
for line in data:
    a = list(map(int, line.split()))
    dec = False
    inc = False
    safe = True
    for i in range(1, len(a)):
        if a[i] == a[i - 1]:
            safe = False
            continue
        if abs(a[i] - a[i - 1]) >= 4:
            safe = False
            continue

        if a[i] > a[i - 1]:
            inc = True
        if a[i] < a[i - 1]:
            dec = True
    if inc and dec:
        safe = False

    if safe:
        cnt += 1
    else:
        unmarked.append(idx)
    idx += 1

for q in unmarked:
    line = data[q]
    a = list(map(int, line.split()))
    for ch in range(len(a)):
        b = list()
        for i in range(len(a)):
            if i != ch:
                b.append(a[i])

        dec = False
        inc = False
        safe = True

        for i in range(1, len(b)):
            if b[i] == b[i - 1]:
                safe = False
                continue
            if abs(b[i] - b[i - 1]) >= 4:
                safe = False
                continue

            if b[i] > b[i - 1]:
                inc = True
            if b[i] < b[i - 1]:
                dec = True
        if inc and dec:
            safe = False

        if safe:
            cnt += 1
            break



print(cnt)

