r, c = map(int, input().split())

sum_row = []
sum_col = [0] * c

for i in range(r):
    row = list(map(int, input().split()))
    sum_row.append(sum(row))

    for j in range(c):
        sum_col[j] += row[j]

print(f'Суммы строк: {sum_row}')
print(f'Суммы столбцов: {sum_col}')
