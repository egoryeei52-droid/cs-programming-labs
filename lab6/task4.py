n = int(input())
if n < 0:
    print('Ошибка')
else:
    if n == 0:
        print('Цифр: 1')
        print('Сумма цифр: 0')
    else:
        count = 0
        sum_n = 0
        while n > 0:
            digit = n % 10
            sum_n += digit
            count += 1
            n //= 10
        print(f'Цифр: {count}')
        print(f'Сумма цифр: {sum_n}')