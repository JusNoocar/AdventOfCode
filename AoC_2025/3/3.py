with open("3.txt") as f:
    data = [line.strip() for line in f.readlines()]

ans = 0
cnt = 12


for line in data:
    dp = [[0 for i in range(len(line))] for i in range(cnt)]

    dp[0][len(line) - 1] = line[-1]
    for i in range(len(line) - 2, -1, -1):
       dp[0][i] = str(max(int(dp[0][i + 1]), int(line[i])))

    for q in range(1, cnt):
       
       dp[q][len(line) - q - 1] = line[len(line) - q - 1] + dp[q - 1][len(line) - q]
       for i in range(len(line) - q - 2, -1, -1):
          dp[q][i] = str(max(int(dp[q][i + 1]), int(line[i] + dp[q - 1][i + 1])))
    
    ans += int(dp[cnt - 1][0])
    print(dp[cnt - 1][0])

print(ans)
