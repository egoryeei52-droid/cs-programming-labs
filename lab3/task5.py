s = input()

print(f'Длина: {len(s)}')
print(f'Только буквы: {s.isalpha()}')
print(f'Только цифры: {s.isdigit()}')
print(f'Буквенно-цифровая: {s.isalnum()}')
print(f'Содержит дефис: {'-' in s}')