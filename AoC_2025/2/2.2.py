with open("2.txt") as f:
    a = [elem.split('-') for elem in f.read().split(',')]
print(a)

ans = 0
yay = set()
for inp in a:
    for k in range(2, 10):
      [x, y] = inp
      #print(x, len(x))
      if len(x) % k != 0:
          x = k * ("1" + (len(x) // k) * "0")
      if len(y) % k != 0:
          y = k * ((len(y) // k) * "9")
      if y == '':
          continue
      #print(x, y)
      mx = len(x) // k
      my = len(y) // k
      right = int(y[:my])
      left = int(x[:mx])
      # now = int(y[:my]) - int(x[:mx])

      for i in range(2, len(x) // mx + 1):
        if int(x[:mx]) > int(x[mx*(i - 1) : i*mx]):
            break
        if int(x[:mx]) < int(x[mx*(i - 1) : i*mx]):
            left += 1
            break
        
      for i in range(2, len(y) // my + 1):
        if int(y[:my]) < int(y[my * (i - 1) : i*my]):
            break
        if int(y[:my]) > int(y[my * (i - 1) : i*my]):
            right -= 1
            break
        
      if right - left >= 0:
          for i in range(left, right + 1):
              yay.add(int(k * str(i)))
        #ans += (right * (right + 1) // 2 - (left - 1) * (left) // 2)
      print(k, k * str(left),  k * str(right))
    print()
for el in yay:
  ans += el

print(ans)
    

