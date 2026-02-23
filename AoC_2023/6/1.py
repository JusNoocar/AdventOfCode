file = "test.txt" 
f = open(file)
data = f.readlines()
time = list(map(int, data[0].split(":")[1].split()))
dist = list(map(int, data[1].split(":")[1].split()))

ans = 1
for i in range(len(time)):
    cnt = 0
    for hold in range(1, time[i]):
        d = (time[i]- hold) * hold
        if d > dist[i]:
            cnt += 1
            
    ans *= cnt
    
print(ans)