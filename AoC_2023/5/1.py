file = "test.txt" 
f = open(file)
data = f.readlines()

seeds = list(map(int, data[0].split(":")[1].split()))
print(seeds)

seed_to_soil = dict()
soil_to_fertilizer = dict()
fertilizer_to_water = dict()
water_to_light = dict()
light_to_temperature = dict()
temperature_to_humidity = dict()
humidity_to_location = dict()

i = 3

while (data[i] != "\n"):
    end, start, rng = map(int, data[i].split())
    
    for j in range(0, rng):
        seed_to_soil[start + j] = end + j
    
    i += 1
    
i += 2
while (data[i] != "\n"):
    end, start, rng = map(int, data[i].split())
        
    for j in range(0, rng):
        soil_to_fertilizer[start + j] = end + j
        
    i += 1

i += 2
while (data[i] != "\n"):
    end, start, rng = map(int, data[i].split())
        
    for j in range(0, rng):
        fertilizer_to_water[start + j] = end + j
        
    i += 1

i += 2
while (data[i] != "\n"):
    end, start, rng = map(int, data[i].split())
        
    for j in range(0, rng):
        water_to_light[start + j] = end + j
        
    i += 1

i += 2
while (data[i] != "\n"):
    end, start, rng = map(int, data[i].split())
        
    for j in range(0, rng):
        light_to_temperature[start + j] = end + j
        
    i += 1

i += 2
while (data[i] != "\n"):
    end, start, rng = map(int, data[i].split())
        
    for j in range(0, rng):
        temperature_to_humidity[start + j] = end + j
        
    i += 1

i += 2
while (i < len(data) and data[i] != "\n"):
    end, start, rng = map(int, data[i].split())
        
    for j in range(0, rng):
        humidity_to_location[start + j] = end + j
        
    i += 1

ans = 0
ch = True
for seed in seeds:
    now = seed
    if now in seed_to_soil:
        now = seed_to_soil[now]
        
    if now in soil_to_fertilizer:
        now = soil_to_fertilizer[now]
    
    if now in fertilizer_to_water:
        now = fertilizer_to_water[now]
    
    if now in water_to_light:
        now = water_to_light[now]
        
    if now in light_to_temperature:
        now = light_to_temperature[now]
        
    if now in temperature_to_humidity:
        now = temperature_to_humidity[now]
        
    if now in humidity_to_location:
        now = humidity_to_location[now]
       
    if ch: 
        ans = now
    else:
        ans = min(ans, now)
        ch = False
        
print(ans)
    
