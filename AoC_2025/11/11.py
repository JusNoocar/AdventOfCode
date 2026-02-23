
topsort = []
def dfs(v, g, used):
  used[v] = True

  if v not in g:
    return
  for u in g[v]:
    if not used[u]:
      dfs(u, g, used)

  topsort.append(v)
    



with open("11.txt") as file:
  g = {line.strip().split(': ')[0] :  line.strip().split(': ')[1].split(' ') for line in file.readlines()}

used = dict()
ways = dict()
for v in g:
  for u in g[v]:
    used[u] = False
    ways[u] = 0
  used[v] = False
  ways[v] = 0

dfs('you', g, used)
topsort = topsort[::-1]

ways['you'] = 1
print(topsort)
for v in topsort:
  if v not in g:
    continue
  for u in g[v]:
    ways[u] += ways[v]

print(ways)
print(ways['out'])
  