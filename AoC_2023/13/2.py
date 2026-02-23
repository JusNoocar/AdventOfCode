def check(a):
    res = []
    n = len(a)
    m = len(a[0]) - 1
    used = False
    for i in range(n - 1):
        #print(i)
        #print()
        flag = True
        for j in range(min(i + 1, n - i - 1)):
            #print(i - j, i + j + 1)
            if a[i + j + 1] != a[i - j]:
                flag = False
        if flag:
            res.append(100 * (i + 1))

    
    for i in range(m - 1):
        #print(i, m)
        #print()
        flag = True
        for j in range(min(i + 1, m - i - 1)):
            s1 = ''
            s2 = ''
                
            for x in range(n):
                s1 = s1 + a[x][i - j]
                s2 = s2 + a[x][i + j + 1]
            #print(s1, s2)
            if s1 != s2:
                flag = False 
        if flag:
            res.append(i + 1)
        #print()
    return res


file = "test.txt" 
f = open(file)
data = f.readlines()

data_idx = 0
a = []
ans = 0
while data_idx < len(data):
    cnt = 0
    if data[data_idx] != '\n':
        a.append(data[data_idx])
    else:
        n = len(a)
        m = len(a[0]) - 1
        used = False
        for i in range(n - 1):
            #print(i)
            #print()
            flag = True
            for j in range(min(i + 1, n - i - 1)):
                #print(i - j, i + j + 1)
                if a[i + j + 1] != a[i - j]:
                    flag = False
            if flag:
                cnt = 100 * (i + 1)
                used = True
                break
            
        if not used:

            for i in range(m - 1):
                #print(i, m)
                #print()
                flag = True
                for j in range(min(i + 1, m - i - 1)):
                    s1 = ''
                    s2 = ''
                    
                    for x in range(n):
                        s1 = s1 + a[x][i - j]
                        s2 = s2 + a[x][i + j + 1]
                    #print(s1, s2)
                    if s1 != s2:
                        flag = False 
                if flag:
                    cnt = (i + 1)
                    used = True
                    break   
                #print()
            
        to_add = 0
        for i in range(n):
            for j in range(m):
                if (a[i][j] == '#'):
                    a[i] = a[i][:j] + '.' + a[i][j+1:]

                    res = check(a)
                    if res != []:
                        for x in range(len(res)):
                            if res[x] != cnt:
                                to_add = res[x]
                    a[i] = a[i][:j] + '#' + a[i][j+1:]
                else:
                    a[i] = a[i][:j] + '#' + a[i][j+1:]
                    res = check(a)
                    if res != []:
                        for x in range(len(res)):
                            if res[x] != cnt:
                                to_add = res[x]  
                    a[i] = a[i][:j] + '.' + a[i][j+1:]
                
        a=[]
        ans += to_add
                
        
                
    #print('ans:', ans)               
    data_idx += 1
    
    

    
print(ans)
