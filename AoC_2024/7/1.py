from itertools import *

f = open('test.txt')
data = f.readlines()

cnt = 0
for line in data:
    s1, s2 = line.strip().split(': ')
    key = int(s1)
    nums = list(map(int, s2.split(' ')))
    check = False
    for x in product('*+',repeat=len(nums) - 1):
        seq = ''.join(x)
        ans = nums[0]
        for i in range(len(nums) - 1):
            if seq[i] == '+':
                ans += nums[i + 1]
            else:
                ans *= nums[i + 1]
        if ans == key:
            check = True
    if check:
        cnt += key

print(cnt)