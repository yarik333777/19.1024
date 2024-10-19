def fakt_divide(first, second):
    integer = float(first)
    float_ = float(second)
    if integer != 0 and float_  != 0:
        return integer / float_
    else:
        print('Ошибка')
i = fakt_divide(6,6)
print(i)
