# # 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100).
# # Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции.
# # По возможности доработайте алгоритм (сделайте его умнее).
# import random as rn
#
# li = list()
# for i in range(20):
#     num = rn.randint(-100,99)
#     li.append(num)
#
#
# def sortw(li):
#     print(f'Исходный массив:\n{li}')
#     n = 1
#     while n < len(li):
#         a = 0
#         for i in range(len(li)-n):
#             if li[i] < li[i+1]:
#                 li[i],li[i+1] = li[i+1],li[i]
#                 a = 1
#         if a == 0:
#             break
#         n += 1
#     print(f'Отсортированный массив:\n{li}')
#     return li
#
# li = sortw(li)




# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.
#
# import  random as rn
#
# def merge_sort(alist, start, end):
#     if end - start > 1:
#         mid = (start + end) // 2
#         merge_sort(alist, start, mid)
#         merge_sort(alist, mid, end)
#         merge_list(alist, start, mid, end)
#
#
# def merge_list(alist, start, mid, end):
#     left = alist[start:mid]
#     right = alist[mid:end]
#     k = start
#     i = 0
#     j = 0
#     while (start + i < mid and mid + j < end):
#         if (left[i] <= right[j]):
#             alist[k] = left[i]
#             i = i + 1
#         else:
#             alist[k] = right[j]
#             j = j + 1
#         k = k + 1
#     if start + i < mid:
#         while k < end:
#             alist[k] = left[i]
#             i = i + 1
#             k = k + 1
#     else:
#         while k < end:
#             alist[k] = right[j]
#             j = j + 1
#             k = k + 1
#
#
# alist = list()
# for i in range(20):
#     number = rn.uniform(0,49)
#     alist.append(number)
# print(f'Список:\n{alist}')
# merge_sort(alist, 0, len(alist))
# print('отсортированный список: ')
# print(alist)
#
#
#
#


# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой называется элемент ряда,
# делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
# Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках
import random as rn

def med(array):
    count = len(array)
    median = -1
    smaller = 0
    larger = 0
    for i in range(count):
        for j in range(count):
            if array[i] < array[j] and i != j:
                larger += 1
            if array[i] >= array[j] and i != j:
                smaller += 1
        if larger == smaller:
            median = array[i]
            break
        else:
            larger = 0
            smaller = 0
    if median == -1:
        raise ValueError
    else:
        return median

n = int(input('Введите натуральное число: '))
clist = list()
if n > 0:
    length = 2*n+1
    for i in range(length):
        clist.append(rn.randint(1,20))
    print(f'Случайный список: {clist}')
    a = med(clist)
    print(f'Медиана: {a}')
else:
    raise ValueError