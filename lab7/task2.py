num = []
for i in input().split():
    num.append(int(i))
sq = []
for x in num:
    if x > 0 and x % 2 != 0:
        sq.append(x**2)
print(f'Квадраты: {sq}')
