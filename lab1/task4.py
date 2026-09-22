dano = 7384
hour = dano // 3600
ost = dano % 3600
min = ost // 60
sec = ost % 60

print(f'{hour:02d}:{min:02d}:{sec:02d}')
