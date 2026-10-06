price = float(input())
age = int(input())
if price < 0 or age < 0 or age > 120:
    print('Ошибка')
elif 0 <= age <= 5: print(f'Стоимость: {price * 0:.2f} руб')
elif 6 <= age <= 17: print(f'Стоимость: {price * 0.5:.2f} руб')
elif 18 <= age <= 59: print(f'Стоимость: {price * 1:.2f} руб')
elif 60 <= age <= 120: print(f'Стоимость: {price * 0.7:.2f} руб')
