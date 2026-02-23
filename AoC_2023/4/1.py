file = "test.txt" 
f = open(file)
cards = f.readlines()

ans = 0
for card in cards:
    score = 0
    name, val = card.split(":")
    win, lst = val.split("|")
    win = list(win.split())
    lst = list(lst.split())
    for num in win:
        if num in lst:
            if score == 0: score = 1
            else: score *= 2
    ans += score
    
print(ans)
