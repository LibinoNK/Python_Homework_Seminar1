# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали
# билет с номером. Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
#
# 385916 -> yes
# 123456 -> no
# ******** Рассмотрите вариант разделения на правую и левую часть произвольно, но не меняя порядок цифр.

number = int(input("Введите номер билета: "))
right_amount = 0
left_amount = 0

while number > 999:
    right_amount += number % 10
    number //= 10
while number > 10:
    left_amount += number % 10
    number //= 10
left_amount += number

if left_amount == right_amount:
    print("Юхууу!!! Билетик счастливый, скорее загадывай желание!")
else:
    print("Не повезло! :с Билетик не счастливый. Повезет в следующий раз!:)")


#Вариант с произвольным разделением

num = input("Введите номер билета: ")
symbol = int(input("Введите после какого символа по счету разделять: ")) - 1

i = 0
left_side = ""
while i <= symbol:
    left_side += num[i]
    i += 1

right_side = ""
while i < len(num):
    right_side += num[i]
    i += 1

left_side = int(left_side)
left_amo = 0
while left_side > 10:
    left_amo = left_side % 10 + left_amo
    left_side //= 10
left_amo += left_side

right_side = int(right_side)
right_amo = 0
while right_side > 10:
    right_amo = right_side % 10 + right_amo
    right_side //= 10
right_amo += right_side

if left_amo == right_amo:
    print("Юхууу!!! Билетик счастливый, скорее загадывай желание!")
else:
    print("Не повезло! :с Билетик не счастливый. Повезет в следующий раз!:)")


