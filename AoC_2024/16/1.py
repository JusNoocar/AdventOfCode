f = open('test.txt')
data = f.readlines()
print(len(data), len(data[0].strip()))