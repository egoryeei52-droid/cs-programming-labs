n  = int(input())
odd = 0
for r in range(n):
    c = 1
    for k in range(r + 1):
        print(c, end = '')
        if c % 2 != 0:
            odd += 1
        if k < r:
            print(' ', end = '')
            c = c * (r - k) // (k + 1)
    print()
print(f'Нечетных элементов: {odd}')
