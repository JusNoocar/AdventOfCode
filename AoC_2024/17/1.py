f = open('test.txt')
data = f.readlines()
a = int(data[0].strip().split(': ')[1])
b = int(data[1].strip().split(': ')[1])
c = int(data[2].strip().split(': ')[1])

prog = list(map(int, (data[4].strip().split(': ')[1]).split(',')))
def get_combo(num):
    global a, b, c
    if 0 <= num <= 3: return num
    if num == 4: return a
    if num == 5: return b
    if num == 6: return c
    print('error')

ptr = 0
out = []
while ptr < len(prog) - 1:
    opcode = prog[ptr]
    literal = prog[ptr + 1]
    combo = get_combo(literal)
    match opcode:
        case 0:
            a = a // (2 ** combo)
        case 1:
            b = b ^ literal
        case 2:
            b = combo % 8
        case 3:
            if a != 0: ptr = literal - 2
        case 4:
            b = b ^ c
        case 5:
            out.append(combo % 8)
        case 6:
            b = a // (2 ** combo)
        case 7:
            c = a // (2 ** combo)
    ptr += 2

print(','.join(map(str, out)))