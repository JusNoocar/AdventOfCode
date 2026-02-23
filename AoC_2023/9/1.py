file = "test.txt" 
f = open(file)
data = f.readlines()

ans = 0
for q in range(len(data)):
    a = list()
    a.append(list(map(int, data[q].split())))
    
    flag = True
    while flag:
        new_list = list()
        
        flag = False
        for i in range(1, len(a[-1])):
            new_list.append(a[-1][i] - a[-1][i - 1])
            if new_list[-1] != 0:
                flag = True
                
        a.append(new_list)
        
    #print(a)
    num = 0
    for i in range(len(a)):
        if len(a[i]) > 0:
            num += a[i][-1]
            
    ans += num
    
print(ans)
            
    
    