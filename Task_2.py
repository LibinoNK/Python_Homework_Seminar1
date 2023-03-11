# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
#
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

# Вариант 1 (через строку)
number = input("Введите трехзначное число: ")

# Проверка на "трехзначность"
while len(number) < 3 or len(number) > 3:
    number = input("Это не трехзначное число! Введите трехзначное число: ")

i = 0
amount = 0

while i < len(number):
    amount += int(number[i])
    i += 1

print(f"Сумма цифр введенного числа равна {amount}")

# Вариант 2 (через математику)
other_number = int(input("Введите трехзначное число: "))

# Проверка на "трехзначность"
while other_number < 100 or other_number > 999:
    other_number = int(input("Это не трехзначное число! Введите трехзначное число: "))

other_amount = 0

while other_number > 10:
    other_amount = other_number % 10 + other_amount
    other_number //= 10
other_amount += other_number

print(f"Сумма цифр введенного числа равна {other_amount}")
