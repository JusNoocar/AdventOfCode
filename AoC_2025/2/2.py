with open("2.txt") as f:
    a = [elem.split('-') for elem in f.read().split(',')]
print(a)

ans = 0
for [x, y] in a:
    if len(x) % 2 != 0:
        x = 2 * ("1" + (len(x) // 2) * "0")
    if len(y) % 2 != 0:
        y = 2 * ((len(y) // 2) * "9")
    mx = len(x) // 2
    my = len(y) // 2
    right = int(y[:my])
    left = int(x[:mx])
    # now = int(y[:my]) - int(x[:mx])
    if int(x[:mx]) < int(x[mx:]):
        left += 1
    if int(y[:my]) > int(y[my:]):
        right -= 1
    if right - left >= 0:
        for i in range(left, right + 1):
            ans += int(str(i) + str(i))
        #ans += (right * (right + 1) // 2 - (left - 1) * (left) // 2)
    print(str(left) + str(left),  str(right) + str(right))

print(ans)
    

