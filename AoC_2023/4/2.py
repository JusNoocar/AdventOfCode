file = "test.txt" 
f = open(file)
cards = f.readlines()


dp = [0 for i in range(len(cards))]
s = 0
for i in range(len(cards) - 1, -1, -1):
    card = cards[i]

    cnt = 0
    name, val = card.split(":")
    win, lst = val.split("|")
    win = list(win.split())
    lst = list(lst.split())
    for num in win:
        if num in lst:
            cnt += 1

    dp[i] += 1
    for j in range(i + 1, min(len(cards), i + 1 + cnt)):
        dp[i] += dp[j]
    #print(dp[i])
    s += dp[i]

print(s)