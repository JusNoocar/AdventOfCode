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

n = len(x)
cnt = 0
for i in range(n):
    name = 'in'
    
    while name != 'A' and name != 'R':
        print(name, end=' ')
        conditions = list(rules[name].split(','))
        
        for j in range(len(conditions)):
            condition = conditions[j]
            if j == len(conditions ) - 1:
                name = condition
                break
            cond, nxt_step = condition.split(':')
            num = int(cond[2:])
            flag = False
            match cond[0]:
                case 'x':
                    if cond[1] == '<' and x[i] < num:
                        flag = True
                    elif cond[1] == '>' and x[i] > num:
                        flag = True
                case 'm':
                    if cond[1] == '<' and m[i] < num:
                        flag = True
                    elif cond[1] == '>' and m[i] > num:
                        flag = True                
                case 'a':
                    if cond[1] == '<' and a[i] < num:
                        flag = True
                    elif cond[1] == '>' and a[i] > num:
                        flag = True                
                case 's':
                    if cond[1] == '<' and s[i] < num:
                        flag = True
                    elif cond[1] == '>' and s[i] > num:
                        flag = True     
            
            if flag:
                name = nxt_step
                break
     
    print(name)   
    if name == 'A':
        cnt += x[i] + m[i] + a[i] + s[i]
        
print(cnt)
            
    
        
        