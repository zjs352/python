# coding=utf-8
#
# list = [10, 1, 35, 61, 89, 36, 55]
# def BubbleSort(list):
#     n = len(list)
#     for i in range(n):
#         for j in range(n-i-1):
#             if list[j] > list[j+1]:
#                 list[j], list[j+1] = list[j+1], list[j]
#     return list
#
# print(BubbleSort(list))
# import random
# list_r = []
# for i in range(1000):
#     num = random.randint(0, 1000)
#     list_r.append(num)
# a = {}
# for i in list_r:
#     if list_r.count(i)>1 :
#         a[i] = list_r.count(i)
# print(a)

# for i in range(1, 10):
#     for j in range(1, i+1):
#         print("%d*%d=%d" % (i, j, i*j)+" ", end='')
#     print('\n')


# def fib(n):
#     if n <= 2:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# print(fib(4))

list = [1, 1]


def fib(n):
    if n <= 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        for i in range(n-2):
            num = list[i] + list[i+1]
            list.append(num)
        return list


