doc = input()
category = doc[:3]
year = doc[4:8]
number = doc[9:13]
reversed_number = number[::-1]

print(f'Категория: {category}')
print(f'Год: {year}')
print(f'Номер: {number}')
print(f'Обратный номер: {reversed_number}')