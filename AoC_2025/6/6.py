with open("6.txt") as f:
    data = [line for line in f.readlines()]
a = [line[:-1] for line in data[:-1]]
print(a)
op = data[-1]
print(op)
big_ans = 0
i = 0
while (i < len(op)):
    nums = []
    check = True
    k = i
    while check and k < len(a[0]):
        check = False
        n = ""
        for j in range(len(a)):
            if a[j][k]!= " ":
                check = True
                n += a[j][k]
        if check:
            nums.append(int(n))
            print(n, " ")
            k += 1
    print()
    ans = nums[0]
    if op[i] == "+":
        for j in range(1, len(nums)):
            ans += nums[j]
    else:
        for j in range(1, len(nums)):
            ans *= nums[j]
    big_ans += ans
    # i += len(nums + 1)
    while all(k < len(a[0]) and a[j][k] == " " for j in range(len(a))):
        k += 1
    i = k
print(big_ans)