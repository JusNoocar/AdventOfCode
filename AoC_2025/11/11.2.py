
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

dfs('svr', g, used)
topsort = topsort[::-1]

ways['svr'] = 1
print(topsort)
for v in topsort:
  if v not in g:
    continue
  for u in g[v]:
    ways[u] += ways[v]

svrdac = ways['dac']
svrfft = ways['fft']



topsort = []
for v in g:
  for u in g[v]:
    used[u] = False
    ways[u] = 0
  used[v] = False
  ways[v] = 0

dfs('dac', g, used)
topsort = topsort[::-1]

ways['dac'] = 1
for v in topsort:
  if v not in g:
    continue
  for u in g[v]:
    ways[u] += ways[v]

dacfft = ways['fft']
dacout = ways['out']



topsort = []
for v in g:
  for u in g[v]:
    used[u] = False
    ways[u] = 0
  used[v] = False
  ways[v] = 0

dfs('fft', g, used)
topsort = topsort[::-1]

ways['fft'] = 1
for v in topsort:
  if v not in g:
    continue
  for u in g[v]:
    ways[u] += ways[v]

fftdac = ways['dac']
fftout = ways['out']

print(svrdac, svrfft, dacfft, fftdac, dacout, fftout)
ans = svrdac * dacfft * fftout + svrfft * fftdac * dacout

print(ans)
  