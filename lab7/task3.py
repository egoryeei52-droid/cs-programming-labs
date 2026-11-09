num = []
for i in input().split():
    num.append(int(i))
target = int(input())
index = []
for i, x in enumerate(num):
    if x == target:
        index.append(i)
print(f'Индексы: {index}')
