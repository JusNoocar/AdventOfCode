file = "test1.txt" 
f = open(file)
games = list(f.readlines())
ans = 0
for i in range(100):
    c = dict()
    c["red"] = 0
    c["green"] = 0
    c["blue"] = 0
    
    g = games[i]
    data = list(g.split(":"))[1]
    turns = data.split(";")
    for turn in turns:
        #print(turn)
        types = turn.split(",")
        for t in types:
            #print(t)
            num = list(t.split())[0]
            num = int(num)
            color = list(t.split())[1]
            c[color] = max(c[color], num)
    ans += c["red"] * c["green"] * c["blue"]

print(ans)
