k = 0
total = 0
while True:
    s = input()
    if s == 'stop':
        break
    price = int(s)
    k += 1
    total += price

if k == 0:
    print('Нет покупок')
else:
    print(f'Покупок: {k}')
    print(f'Общая стоимость: {total} руб')
    print(f'Средняя стоимость: {total / k:.2f} руб')
    