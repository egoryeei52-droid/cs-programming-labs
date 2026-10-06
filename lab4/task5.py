year = int(input())
if year < 1 or year > 9999: print ('Ошибка')
elif year % 400 == 0: print('Високосный')
else: print('Невисокосный')
