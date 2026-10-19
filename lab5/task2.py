a = int(input())
b = int(input())
s = 0
u = 1
for x in range(a, b + 1):
    s += x
    u *= x
print(f'Сумма: {s}')
print(f'Произведение: {u}')
