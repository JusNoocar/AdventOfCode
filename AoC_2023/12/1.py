file = "test.txt" 
f = open(file)
data = f.readlines()

ans = 0
for line in data:
    s, nums = line.split();
    n = len(s)
    c = list(map(int, nums.split(',')))
    dp = [[0 for i in range(len(c))] for j in range(n)]
    
    for i in range(n - 1, -1, -1):
        for j in range(len(c) - 1, -1, -1):
            flag = True
            if i + c[j] > n:
                flag = False
                
            
            for x in range(i, min(i + c[j], n)):
                if s[x] == '.': flag = False
                
            if i + c[j] < n and s[i + c[j]] == '#':
                flag = False
                
            
            if j != len(c) - 1 and flag:
                for x in range(i + c[j] + 1, n):
                    if s[x] == '#' or s[x] == '?':
                        dp[i][j] += dp[x][j + 1]
                        
                    if s[x] == '#':
                        break
            elif flag:
                for x in range(i + c[j] + 1, n):
                    if s[x] == '#': flag = False
                    
                if flag:
                    dp[i][j] += 1
            #print(dp[i][j], end = ' ')
        #print()
        
    
    cnt = 0
    for x in range(n):
        if s[x] == '#' or s[x] == '?':
            cnt += dp[x][0]
            
        if s[x] == '#':
            break
    print('cnt: ',cnt)
    
    ans += cnt
    
print(ans)

    
                