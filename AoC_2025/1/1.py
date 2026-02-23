with open("1.txt") as f:
    data = [line.strip() for line in f.readlines()]

cnt = 50
ans = 0
for line in data:
    num = int(line[1:])
    ans += num // 100
    num %= 100
    if line[0] == 'L':
        if (cnt - num <= 0 and cnt > 0):
            ans += 1
        cnt = (100 + cnt - num) % 100
    else:
        if (cnt + num >= 100):
            ans += 1
        cnt = (cnt + num) % 100
    #print(ans)
print(ans)