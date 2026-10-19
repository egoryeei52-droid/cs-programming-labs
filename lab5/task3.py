n = int(input())
below = 0
zero = 0
above = 0
for _ in range(n):
    t = float(input())
    if t < 0:
        below += 1
    elif t == 0:
        zero += 1
    else:
        above += 1
print(f'Ниже нуля: {below}')
print(f'Равны нулю: {zero}')
print(f'Выше нуля: {above}')
