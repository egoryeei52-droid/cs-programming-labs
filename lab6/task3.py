n = int(input())
if n < 2:
    print('Ошибка')
else:
    factors = []
    i = 2
    while i**2 <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1
    if n > 1:
        factors.append(n)
    print(*factors)
