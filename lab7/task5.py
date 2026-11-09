r, c = map(int, input().split())

table = []
for _ in range(r):
    table.append(list(map(int, input().split())))

row_start, row_end, col_start, col_end = map(int, input().split())

target = int(input())

found = False

for i in range(row_start, row_end + 1):
    for j in range(col_start, col_end + 1):
        if table[i][j] == target:
            print(i, j)
            found = True
if not found:
    print('Не найдено')
