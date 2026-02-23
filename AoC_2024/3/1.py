f = open("test.txt")
data = f.read()
print(data)
step = 0
ans = 0
num1 = 0
num2 = 0
enabled = True
print(data[4 - 3 : 5])
for i in range(3, len(data)):
    if data[i - 3: i + 1] == "do()":
        enabled = True
        num1 = 0
        num2 = 0
        step = 0
    if i >= 6 and data[i - 6: i + 1] == "don't()":
        enabled = False
        num1 = 0
        num2 = 0
        step = 0
    if data[i - 3: i + 1] == "mul(":
        step = 1
    elif step == 1 or step == 2 and data[i].isdigit():
        num1 *= 10
        num1 += int(data[i])
        step = 2
    elif step == 2 and data[i] == ',':
        step = 3
    elif step == 3 or step == 4 and data[i].isdigit():
        num2 *= 10
        num2 += int(data[i])
        step = 4
    elif step == 4 and data[i] == ")":
        if num1 < 1000 and num2 < 1000 and enabled:
            ans += num1 * num2
        num1 = 0
        num2 = 0
        step = 0
    else:
        num1 = 0
        num2 = 0
        step = 0

print(ans)