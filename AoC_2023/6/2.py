file = "test.txt" 
f = open(file)
data = f.readlines()
time = int("".join(data[0].split(":")[1].split()))
dist = int("".join(data[1].split(":")[1].split()))

ans = 1
for i in range(1):
    cnt = 0
    for hold in range(1, time):
        d = (time- hold) * hold
        if d > dist:
            cnt += 1
            
    ans *= cnt
    
print(ans)