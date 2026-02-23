rules = dict()

x = []
m = []
a = []
s = []
step = 0

ans = 0

def count(nameinp, xinp, minp, ainp, sinp):
    name = nameinp[:]
    xb = xinp[:]
    mb = minp[:]
    ab = ainp[:]
    sb = sinp[:]
    global ans, rules
    
    print(name)
    print(xb, mb, ab, sb)
    
    if xb[0] >= xb[1] or mb[0] >= mb[1] or ab[0] >= ab[1] or sb[0] >= sb[1]:
        return
    if name == 'A':
        ans += (xb[1] - xb[0]) * (mb[1] - mb[0]) * (ab[1] - ab[0]) * (sb[1] - sb[0])
        return
    
    if name == 'R':
        return
    
    
    conditions = list(rules[name].split(','))
        
    for j in range(len(conditions)):
        condition = conditions[j]
        #print(condition, end=' ')
        if j == len(conditions) - 1:
            name = condition[:]
            break
        cond, nxt_step = condition.split(':')
        num = int(cond[2:])

        match cond[0]:
            case 'x':
                if cond[1] == '<':
                    next_xb = xb[:]
                    next_xb[1] = min(next_xb[1], num)
                    count(nxt_step[:], next_xb[:], mb[:], ab[:], sb[:])
                    
                    xb[0] = max(xb[0], num)
                elif cond[1] == '>':
                    next_xb = xb[:]
                    next_xb[0] = max(next_xb[0], num + 1)
                    count(nxt_step[:], next_xb[:], mb[:], ab[:], sb[:])
                    
                    xb[1] = min(xb[1], num + 1)         
            case 'm':
                if cond[1] == '<':
                    next_mb = mb[:]
                    next_mb[1] = min(next_mb[1], num)
                    count(nxt_step[:], xb[:], next_mb[:], ab[:], sb[:])
                    
                    mb[0] = max(mb[0], num)                    
                elif cond[1] == '>':
                    #print('num', num)
                    next_mb = mb[:]
                    next_mb[0] = max(next_mb[0], num + 1)
                    count(nxt_step[:], xb[:], next_mb[:], ab[:], sb[:])
                    
                    mb[1] = min(mb[1], num + 1)                                     
            case 'a':
                if cond[1] == '<':
                    next_ab = ab[:]
                    next_ab[1] = min(next_ab[1], num)
                    count(nxt_step[:], xb[:], mb[:], next_ab[:], sb[:])
                    
                    ab[0] = max(ab[0], num)
                elif cond[1] == '>':
                    next_ab = ab[:]
                    next_ab[0] = max(next_ab[0], num + 1)
                    count(nxt_step[:], xb[:], mb[:], next_ab[:], sb[:])
                    
                    ab[1] = min(ab[1], num + 1)                 
            case 's':
                if cond[1] == '<':
                    next_sb = sb[:]
                    next_sb[1] = min(next_sb[1], num)
                    count(nxt_step[:], xb[:], mb[:], ab[:], next_sb[:])
                    
                    sb[0] = max(sb[0], num)
                elif cond[1] == '>':
                    next_sb = sb[:]
                    next_sb[0] = max(next_sb[0], num + 1)
                    count(nxt_step[:], xb[:], mb[:], ab[:], next_sb[:])
                    
                    sb[1] = min(sb[1], num + 1)
    print('last: ', name, xb, mb, ab, sb)
    count(name[:], xb[:], mb[:], ab[:], sb[:])

    print()

file = "test.txt" 
f = open(file)
data = f.readlines()

rules = dict()

x = []
m = []
a = []
s = []
step = 0
for i in range(len(data)):
    line = data[i]
    if line == '\n':
        step = 1
    elif step == 0:
        name, func = line.split('{')
        func = func[:-2]
        rules[name] = func
        #print(name, func)
    else:
        if i == len(data) - 1: line = line[1: - 1]
        else: line = line[1:-2]
        vals = list(line.split(','))
        #print(vals)
        x.append(int(vals[0][2:]))
        m.append(int(vals[1][2:]))
        a.append(int(vals[2][2:]))
        s.append(int(vals[3][2:]))
#print(x)
#print(m)
#print(a)
#print(s)
xbounds = [1, 4001]
mbounds = [1, 4001]
abounds = [1, 4001]
sbounds = [1, 4001]
n = len(x)

name = 'in'
count(name, xbounds, mbounds, abounds, sbounds)

print(ans)