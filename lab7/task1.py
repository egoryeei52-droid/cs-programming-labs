numbers = [12, -3, 0, 7, -1]
num = numbers.copy()
for i in range(len(num)):
    if num[i] < 0:
        num[i] = 0
print(f'Исходные остатки: {numbers}')
print(f'Исправленные остатки: {num}')
