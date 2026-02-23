file = "test.txt" 
f = open(file)
data = f.readlines()

data_idx = 0
a = []
ans = 0
while data_idx < len(data):
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
                ans += 100 * (i + 1)
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
                    ans += (i + 1)
                    used = True
                    break   
                #print()
                
        a=[]
                
        
                
    #print('ans:', ans)               
    data_idx += 1
    
    

    
print(ans)
        