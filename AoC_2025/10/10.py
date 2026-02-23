from itertools import chain, combinations

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

with open("10.txt") as f:
    a = [line.strip().split(' ') for line in f.readlines()]


def get_field(n, groups):
  field = ['.'] * n
  for button in groups:
      for b in button:
        if field[b] == '.':
            field[b] = '#'
        else:
            field[b] = '.'
  return '[' + ''.join(field) + ']'


def get_f(n, groups, goal):
    # groups: list of lists of indices touched by each button
    # goal: desired counter values

    m = len(groups)
    best = None

    # Upper bound: in worst case, no counter is incremented more than its goal sum
    # A simple but safe bound per button is sum(goal).
    max_presses = sum(goal)

    # DFS over buttons with pruning
    def dfs(idx, cur_goal, cur_sum):
        nonlocal best
        if best is not None and cur_sum >= best:
            return
        if idx == m:
            if all(x == 0 for x in cur_goal):
                best = cur_sum
            return

        # Try pressing button idx k times
        # k cannot exceed max_presses, but we can also cap by min(cur_goal[j]) over j in groups[idx]
        touched = groups[idx]
        if touched:
            cap = min(cur_goal[j] for j in touched)
        else:
            cap = 0
        cap = min(cap, max_presses - cur_sum)

        # k from 0..cap
        for k in range(cap + 1):
            if k > 0:
                for j in touched:
                    cur_goal[j] -= 1
            dfs(idx + 1, cur_goal, cur_sum + k)
        # restore cur_goal after loop
        for j in touched:
            cur_goal[j] += cap

    dfs(0, goal[:], 0)
    return best if best is not None else -1

                 
ans = 0
ans2 = 0
for line in a:
    field = line[0]
    n = len(field) - 2
    buttons = line[1:-1]
    jolt = list(map(int, line[-1][1:-1].split(',')))
    print(field)
    print(buttons)

    global groups
    groups = list()
    for button in buttons:
      v = set(map(int, button[1:-1].split(',')))
      groups.append(v)
    
    power = powerset(groups)
    check = False
    min_ans = 1000000
    min_2 = 1000000
    for p in power:
      #print(p, get_field(n, p))
      if field == get_field(n, p):
          print(p, "Yes!")
          check = True
          min_ans = min(min_ans, len(p))
      p = [list(x) for x in p]
      yay = get_f(n, p, jolt)
      if yay != -1:
          print(p, "Yaaah")
          min_2 = yay
    ans += min_ans
    ans2 += min_2


    # check = True
    # while check == True:
    #   check = False
    #   for u in groups.copy():
    #     if len(u.intersection(v)) == 0:
    #        continue
    #     s = u.symmetric_difference(v)
    #     print(s, end=', ')
    #     if len(s) != 0 and s not in groups:
    #       groups.append(s)
    #       check = True
    #   print(groups)
    # print(groups)
    print()
print(ans)
print(ans2)
      
