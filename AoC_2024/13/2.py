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
    prize_xy = [int(prize[0][2:]) + 10000000000000, int(prize[1][2:]) + 10000000000000]

    x_a = button_a_xy[0]
    y_a = button_a_xy[1]
    x_b = button_b_xy[0]
    y_b = button_b_xy[1]
    X = prize_xy[0]
    Y = prize_xy[1]

    if (X * y_b - x_b * Y) % (x_a * y_b - x_b * y_a) != 0:
        continue
    cnt_a = (X * y_b - x_b * Y) // (x_a * y_b - x_b * y_a)

    if (Y - y_a * cnt_a) % y_b != 0:
        continue
    cnt_b = (Y - y_a * cnt_a) // y_b

    price = cnt_a * 3 + cnt_b
    total_price += price


print(total_price)
