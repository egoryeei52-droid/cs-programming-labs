information = input()

parts = information.split(';')

print(f'Поезд: {parts[0]}')
print (f'Маршрут: {parts[1]} - {parts[2]}')
print(f'Отправление: {parts[3]}')
print(f'Цена: {parts[4]}')