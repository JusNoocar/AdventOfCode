f = open('test.txt')
data = f.readlines()

total_price = 0
n = (len(data) + 1) // 4
for i in range(0, len(data), 4):
    button_a = data[i].split(': ')[1].split(', ')
    button_a_xy = [int(button_a[0][2:]), int(button_a[1][2:])]
    button_b = data[i + 1].split(': ')[1].split(', ')
    button_b_xy = [int(button_b[0][2:]), int(button_b[1][2:])]
    prize = data[i + 2].split(': ')[1].split(', ')
    prize_xy = [int(prize[0][2:]), int(prize[1][2:])]

    min_price = 1000000000
    for cnt_b in range(0, 101):
        left = [prize_xy[0] - button_b_xy[0] * cnt_b, prize_xy[1] - button_b_xy[1] * cnt_b]
        if (left[0] % button_a_xy[0] == 0) and (left[1] % button_a_xy[1] == 0):
            if (left[0] // button_a_xy[0]) == (left[1] // button_a_xy[1]):
                cnt_a = left[0] // button_a_xy[0]
                if cnt_a * 3 + cnt_b < min_price:
                    min_price = cnt_a * 3 + cnt_b
    if min_price != 1000000000:
        total_price += min_price

print(total_price)
