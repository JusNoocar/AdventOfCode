from math import lcm

file = open('test.txt','r')
data = file.readlines()
#print(data)

path = data[0][:-1]

nodes = []
#print(path)
g = dict()
for i in range(2, len(data)):
    v, u1_u2 = data[i].split(' = ')
    if i == len(data) - 1:
        u1, u2 = u1_u2[1: -1].split(', ')
    else:
        u1, u2 = u1_u2[1: -2].split(', ')
    g[v] = [u1, u2]
    if v[-1] == 'A':
        nodes.append(v)
    #print(v, u1, u2)

#v = 'AAA'
ans = -1787
nums = list()
for j in range(len(nodes)):
    add = -13132
    for i in range(1000000):
        idx = i % len(path)
   
        if path[idx] == 'L':
            nodes[j] = g[nodes[j]][0]
        else:
            nodes[j] = g[nodes[j]][1]
        
        if nodes[j][-1] == 'Z':
            add = i
            break
        #print(nodes[j], end=' ')
    nums.append(add + 1)
    #print()


print(nodes)
k = 1
for i in range(0, len(nums)):
    k = lcm(k, nums[i])


print(k)