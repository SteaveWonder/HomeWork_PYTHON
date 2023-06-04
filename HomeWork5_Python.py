# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

# a = int(input('Input A: '))
# b = int(input('Input B: '))

# def SumExpo(a, b):
#     if b == 0:
#         return 1
#     return a * SumExpo(a, b - 1)

# print(f'Expo of number A is: {SumExpo(a, b)}')



# Задача 28: Вводится десятичное число. Реализовать алгоритм его перевода в двоичную систему счисления через рекурсию. 
# Нельзя использовать функцию bin()
# 10
# *Вывод:*
# 1010

# подсказали оба варианта

# var1
# a = int(input("Input num: "))
# l = []
# def convert(b):
#     if (b == 0):
#         return l
#     num = b % 2
#     l.append(num)
#     convert(b // 2)
# convert(a)
# l.reverse()
# for i in l:
#     print(i)


# var2
# def convert(N):
#     if N >= 2:
#         convert(N // 2)
#     print(N % 2, end = '')
  
# convert(19)        