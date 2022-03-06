duration = int(input('Укажите значение в секундах:' ))
d, h, m, s = duration // 86400, duration // 3600, duration // 60 % 60, duration % 60
print(f'{d} дн {h} час {m} мин {s} cек')
