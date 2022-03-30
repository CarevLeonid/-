# 1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
# import cProfile
#
#
# def main():
#     counter = 0
#     for i in range(32,128):
#         counter += 1
#         print(f'{i}: {chr(i)}', end='; ')
#         if counter == 10:
#             print('\n')
#             counter = 0
#
# cProfile.run('main()')
#



# 205 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 4.py:6(main)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#        96    0.000    0.000    0.000    0.000 {built-in method builtins.chr}
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#       105    0.001    0.000    0.001    0.000 {built-in method builtins.print}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#  Четко наблюдается линейная зависимость между количеством операций и количеством данных в диапазоне range(32,128)
#  O(n) – линейная сложность


# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
# Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов. Результаты анализа сохранить в виде комментариев в файле с кодом.

# import cProfile
# #
# def myFunc(n):
#     result = list()
#     for i in range(2, n):
#         simple_num = True
#         for j in range(2, i):
#             if i % j == 0:
#                 simple_num = False
#                 break
#         if simple_num:
#             result.append(i)
#     return result
#
# bez_erat = myFunc(30)
# print(bez_erat)
#
# cProfile.run('myFunc(1000)')
#
# 172 function calls in 0.029 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.022    0.022    0.022    0.022 4.py:43(myFunc)
#         1    0.000    0.000    0.022    0.022 <string>:1(<module>)
#         1    0.006    0.006    0.029    0.029 {built-in method builtins.exec}
#       168    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#

import cProfile
def Eratosfen(n):

    result = [item for item in range(n+1)]
    result[1] = 0
    for i in result:
        if i != 0:
            square = i**2
            for j in range(square,n+1,i):
                result[j] = 0
    result = set(result)
    result.remove(0)
    return list(result)


erat = Eratosfen(30)
print(erat)

cProfile.run('Eratosfen(1000)')

# 6 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 4.py:73(Eratosfen)
#         1    0.000    0.000    0.000    0.000 4.py:75(<listcomp>)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.000    0.000    0.000    0.000 {method 'remove' of 'set' objects}
#
#
# Ввиду того, что метод решения задачи с помощью решета Эратосфена подразумевает собой меньшее количество итераций циклов из-за
# "зачеркиваний" кратных чисел, данный метод является оптимальным