def get_dist(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    return dx*dx + dy*dy

def check_intersection(p1, p2, s1, s2):
    if s1[0] == s2[0]: #horizontal segment
        left, right = min(p1[1], p2[1]), max(p1[1], p2[1])
        if (min(p1[0], p2[0]) < s1[0] and s1[0] < max(p1[0], p2[0])) and \
           (min(s1[1], s2[1]) < right and max(s1[1], s2[1]) > left):
            return True
    if s1[1] == s2[1]: #vertical segment
        left, right = min(p1[0], p2[0]), max(p1[0], p2[0])
        if (min(p1[1], p2[1]) < s1[1] and s1[1] < max(p1[1], p2[1])) and \
           (min(s1[0], s2[0]) < right and max(s1[0], s2[0]) > left):
            return True
    return False

with open("9.txt") as f:
    a = [list(map(int, line.strip().split(','))) for line in f.readlines()]

b = set(x for x in range(len(a)))
next = dict()
for i in range(len(a)):
    next[i] = i + 1
next[len(a) - 1] = 0
# p1 = 0
# print(a[p1], end = ' ')
# b.remove(p1)
# while len(b) != 0:
#     best = None
#     for p2 in b:
#         if (a[p1][0] == a[p2][0] or a[p1][1] == a[p2][1]) and \
#             (best == None or get_dist(a[p1], a[p2]) < get_dist(a[p1], a[best])):
#                 best = p2
#     next[p1] = best
#     print(a[best], end = ' ')
#     p1 = best
#     b.remove(p1)
# next[p1] = 0
# print()

ans = 0
for p1 in a:
  for p2 in a:
      if p1 == p2: continue
      check = True
      st = 0
      while next[st] != 0:
          if check_intersection(p1, p2, a[st], a[next[st]]):
              check = False
          st = next[st]
      if check_intersection(p1, p2, a[st], a[next[st]]):
          check = False
      if check:
          area = (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)
          ans = max(area, ans)
print(ans)

    