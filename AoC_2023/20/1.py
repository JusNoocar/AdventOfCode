modules = dict()
flip_flops = dict()
conjunctions = dict()
types = dict()
inputs = dict()
global high_cnt, low_cnt, button_press
def pulse(name_init, freq_init):
    global high_cnt, low_cnt
    que = []
    que.append([name_init, freq_init, -1])
    while len(que) != 0:
        name = que[0][0]
        freq = que[0][1]
        parent = que[0][2]
        #print(name, freq)
        que.pop(0)
        
        
        if name == 'rx' and freq == 'low':
            print(button_press)
            return
        
        
        if freq == 'low':
            low_cnt += 1
        else:
            high_cnt += 1
        if name == 'broadcaster':
            for m in modules[name]:
                que.append([m, freq, name])
                #pulse(m, freq)
        
        elif name in types and types[name] == '%':
            #print(flip_flops[name])
            if freq == 'low':
                if flip_flops[name] == 0:
                    flip_flops[name] = 1
                    for m in modules[name]:
                        que.append([m, 'high', name])
                        #pulse(m, 'high')
    
                else:
                    flip_flops[name] = 0
                    for m in modules[name]:
                        que.append([m, 'low', name])
                        #pulse(m, 'low')
    
        elif name in types and types[name] == '&':
            if freq == 'low':
                inputs[name][parent] = 0
            else:
                inputs[name][parent] = 1
                
            flag = True
            for key, val in inputs[name].items():
                if val != 1:
                    flag = False
                conjunctions[name] = 0
            if flag:
                for m in modules[name]:
                    que.append([m, 'low', name])
                #pulse(m, 'low')
            else:
                for m in modules[name]:
                    que.append([m, 'high', name])
                #pulse(m, 'high')
    


file = "test.txt" 
f = open(file)
data = f.readlines()

idx = 0
for line0 in data:
    line = line0.strip()

    name, vals = line.split(' -> ')
    
    if name != 'broadcaster':
        if name[0] == '&':
            name = name[1:]
            conjunctions[name] = 1
            types[name] = '&'
            inputs[name] = dict()
        if name[0] == '%':
            name = name[1:]
            flip_flops[name] = 0
            types[name] = '%'
        
    nxt_names = list(vals.split(', '))
    modules[name] = nxt_names
    idx += 1
    
for key, val in modules.items():
    for el in val:
        if el in types and types[el] == '&':
            if key not in inputs[el]:
                inputs[el][key] = 0
  
low_cnt = 0
high_cnt = 0
button_press = 0
print(types)
print(flip_flops)
print(conjunctions)

for i in range(1000000000):
    button_press += 1
    pulse('broadcaster', 'low')
    #print()
    
#print(low_cnt, high_cnt)
#print(low_cnt * high_cnt)