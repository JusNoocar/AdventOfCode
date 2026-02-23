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
for i in range(1000000):
    idx = i % len(path)
    flag = True
    for j in range(len(nodes)):
        if path[idx] == 'L':
            nodes[j] = g[nodes[j]][0]
        else:
            nodes[j] = g[nodes[j]][1]
        
        if nodes[j][-1] != 'Z':
            flag = False
        #print(nodes[j], end=' ')

    #print()


    if flag:
        ans = i
        break

print(nodes)

print(ans + 1)