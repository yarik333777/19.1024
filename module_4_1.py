from fake_math import fakt_divide as f1
from true_math import true_divide as t2

i = f1(69, 3)
print(i)
k = f1(3, 0)
print(k)
p = t2(49, 7)
print(p)
u = t2(15, 0)
print(u)


# В fake_math создайте функцию divide, которая принимает два параметра first и second.
# Функция должна возвращать результат деления first на second,
# но когда в second записан 0 - возвращать строку 'Ошибка'.

# В true_math создайте функцию divide, которая принимает два параметра first и second.
# Функция должна возвращать результат деления first на second,
# но когда в second записан 0 - возвращать бесконечность.
# Бесконечность можно импортировать из встроенной библиотеки math (from math import inf
