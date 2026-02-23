f = open('test.txt')
data = f.readlines()


def run(design, idx):
    print(idx)
    global checker
    global alph
    if idx == len(design):
        checker = True
        return
    letter = design[idx]
    for pattern in alph[letter]:
        if (len(pattern) <= len(design) - idx) and (design[idx: idx + len(pattern)] == pattern):
            run(design, idx + len(pattern))

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
cnt = 0
for design in designs:
    #checker = False
    #run(design, 0)
    #if checker:
    #    cnt += 1
    #print('done')
    ans = [0 for i in range(len(design))]
    for i in range(0, len(design)):
        if design[: i + 1] in alph[design[: i + 1][0]]:
            ans[i] += 1
        for j in range(0, i):
            cut = design[j + 1 : i + 1]
            if cut in alph[cut[0]]:
                ans[i] += ans[j]
    if ans[len(design) - 1] > 0:
        cnt += 1

print(cnt)

