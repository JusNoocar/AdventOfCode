file = "test.txt" 
f = open(file)
data = f.readlines()

seeds = list(map(int, data[0].split(":")[1].split()))
print(seeds)

seed_to_soil = list()
soil_to_fertilizer = list()
fertilizer_to_water = list()
water_to_light = list()
light_to_temperature = list()
temperature_to_humidity = list()
humidity_to_location = list()

i = 3

while (data[i] != "\n"):
    inp = list(map(int, data[i].split()))
    
    seed_to_soil.append([])
    seed_to_soil[-1] = inp
    
    i += 1
    
i += 2
while (data[i] != "\n"):
    inp = list(map(int, data[i].split()))
        
    soil_to_fertilizer.append([])
    soil_to_fertilizer[-1] = inp
        
    i += 1

i += 2
while (data[i] != "\n"):
    inp = list(map(int, data[i].split()))
        
    fertilizer_to_water.append([])
    fertilizer_to_water[-1] = inp
        
    i += 1

i += 2
while (data[i] != "\n"):
    inp = list(map(int, data[i].split()))
        
    water_to_light.append([])
    water_to_light[-1] = inp
        
    i += 1

i += 2
while (data[i] != "\n"):
    inp = list(map(int, data[i].split()))
        
    light_to_temperature.append([])
    light_to_temperature[-1] = inp
        
    i += 1

i += 2
while (data[i] != "\n"):
    inp = list(map(int, data[i].split()))
        
    temperature_to_humidity.append([])
    temperature_to_humidity[-1] = inp
        
    i += 1

i += 2
while (i < len(data) and data[i] != "\n"):
    inp = list(map(int, data[i].split()))
        
    humidity_to_location.append([])
    humidity_to_location[-1] = inp
        
    i += 1

print(light_to_temperature)
ans = 10000000000000000
l = 0
r = 10000000000000000
while (r - l > 1):
    loc = (l + r) / 2
    
    now = loc
    #print(now, end=" ")
    for el in humidity_to_location:
        start, end, rng = el
        if start - rng <= now - rng < start:
            now = end + (now - start)
            break
        
    #print(now, end=" ")
    for el in temperature_to_humidity:
        start, end, rng = el
        if start - rng <= now - rng < start:
            now = end + (now - start)
            break
    
    #print(now, end=" ")
    for el in light_to_temperature:
        start, end, rng = el
        if start - rng <= now - rng < start:
            now = end + (now - start)
            break
        
    
    #print(now, end=" ")
    for el in water_to_light:
        start, end, rng = el
        if start - rng <= now - rng < start:
            now = end + (now - start)
            break
        
        
    #print(now, end=" ")
    for el in fertilizer_to_water:
        start, end, rng = el
        if start - rng <= now - rng < start:
            now = end + (now - start)
            break
    
        
    #print(now, end=" ")
    for el in soil_to_fertilizer:
        start, end, rng = el
        if start - rng <= now - rng < start:
            now = end + (now - start)
            break
    
    for el in seed_to_soil:
        start, end, rng = el
        if start - rng <= now - rng < start:
            now = end + (now - start)
            break
       
    #print(now)
    
    flag = False
    
    for idx in range(1, len(seeds), 2):
        if seeds[idx - 1] <= now < seeds[idx - 1] + seeds[idx]:
            flag = True
    #print(now, flag)
    if flag:
        r = loc
    else:
        l = loc
        
print(r)
    
