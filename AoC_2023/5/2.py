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
ans = 0
ch = True

used = dict()
for idx in range(1, len(seeds), 2):
    print(idx)
    start_data = seeds[idx - 1]
    rng_data = seeds[idx]
    
    for seed in range(start_data, start_data + rng_data):
        if seed in used:
            now = used[seed]
            if ch: 
                ans = now
                ch = False
            else:
                ans = min(ans, now)
            continue
        
        now = seed
        
        for el in seed_to_soil:
            end, start, rng = el
            if start - rng <= now - rng < start:
                now = end + (now - start)
                break
        
        #print(now, end=" ")
        for el in soil_to_fertilizer:
            end, start, rng = el
            if start - rng <= now - rng < start:
                now = end + (now - start)
                break
        
        #print(now, end=" ")
        for el in fertilizer_to_water:
            end, start, rng = el
            if start - rng <= now - rng < start:
                now = end + (now - start)
                break
        
        #print(now, end=" ")
        for el in water_to_light:
            end, start, rng = el
            if start - rng <= now - rng < start:
                now = end + (now - start)
                break
            
        #print(now, end=" ")
        for el in light_to_temperature:
            end, start, rng = el
            if start - rng <= now - rng < start:
                now = end + (now - start)
                break
            
            
        #print(now, end=" ")
        for el in temperature_to_humidity:
            end, start, rng = el
            if start - rng <= now - rng < start:
                now = end + (now - start)
                break
            
            
        #print(now, end=" ")
        for el in humidity_to_location:
            end, start, rng = el
            if start - rng <= now - rng < start:
                now = end + (now - start)
                break
           
        #print(now)
        used[seed] = now
        if ch: 
            ans = now
            ch = False
        else:
            ans = min(ans, now)
        
print(ans)
    
