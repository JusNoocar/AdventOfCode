f = open('test.txt')
data = f.readlines()

patterns = list(data[0].strip().split(', '))
print(len(patterns))
designs = [x.strip() for x in data[2:]]
print(len(designs))
alph = dict()
for pattern in patterns:
    if pattern[0] not in alph:
        alph[pattern[0]] = []
    alph[pattern[0]].append(pattern)
mx = -1
for letter in alph:
    mx = max(mx, len(alph[letter]))
print(mx)
sum = 0
for design in designs:
    ans = [0 for i in range(len(design))]
    for i in range(0, len(design)):
        if design[: i + 1] in alph[design[: i + 1][0]]:
            ans[i] += 1
        for j in range(0, i):
            cut = design[j + 1 : i + 1]
            if cut in alph[cut[0]]:
                ans[i] += ans[j]
    sum += ans[len(design) - 1]

print(sum)

