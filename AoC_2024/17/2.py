def get_combo(num, a, b, c):
    if 0 <= num <= 3: return num
    if num == 4: return a
    if num == 5: return b
    if num == 6: return c
    print('error')

def run_program(prog: list, a: int, b: int, c: int):
    ptr = 0
    out = []
    while ptr < len(prog) - 1:
        opcode = prog[ptr]
        literal = prog[ptr + 1]
        combo = get_combo(literal, a, b, c)
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
    #print(out)
    return out

def run_back(prog: list, b, c):
    ptr = len(prog) - 2
    vals = [0]
    idx = len(prog) - 1
    while ptr > - 1:
        opcode = prog[ptr]
        print(opcode)
        literal = prog[ptr + 1]
        if opcode == 3:
            print("ok")
            new_vals = []
            for val in vals:
                for add in range(8):
                    new_val = val * 8 + add
                    check = new_val
                    while check >= 8:
                        check //= 8
                    if run_program(prog, new_val, b , c)[0] == prog[idx]:
                        new_vals.append(new_val)
            #vals.extend(new_vals)
            vals = new_vals
            idx -= 1
            if idx == -1:
                print(vals)
                break
        elif opcode == 454:
            if a != 0: ptr = literal - 2
        print(vals)
    return min(vals)




f = open('test.txt')
data = f.readlines()
a = int(data[0].strip().split(': ')[1])
b = int(data[1].strip().split(': ')[1])
c = int(data[2].strip().split(': ')[1])

prog = list(map(int, (data[4].strip().split(': ')[1]).split(',')))

print(run_back(prog, b, c))