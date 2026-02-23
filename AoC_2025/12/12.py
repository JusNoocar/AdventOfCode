with open("12.txt") as file:
  data = [line.strip() for line in file.readlines()]

c = [6, 5, 7, 7, 7, 7]
ans = 0
for line in data:
  sz, vals = line.split(": ")
  sz = list(map(int, sz.split("x")))
  vals = list(map(int, vals.split(" ")))
  all_boxes = (sz[0] // 3) * (sz[1] // 3)
  all_c = 0
  for i in range(6):
    all_c += c[i] * vals[i]
  if sz[0] * sz[1] < all_c:
    continue
  ans += 1

print(ans)
