#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# s = (x * x for x in range(5))
# print(s)
# for x in s:
#     print(x)

# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1

# x = fib(10)
# print next(x)
# print next(x)
# print next(x)

# -*- coding: utf-8 -*-

# def triangles():
#     L = [1]
#     while True:
#         yield L
#         L.append(0)
#         L = [L[i - 1] + L[i] for i in range(len(L))]

# n = 0
# for t in triangles():
#     print(t)
#     n = n + 1
#     if n == 10:
#         break


# def triangle():
#       L = [0, 1, 0]
#       while True:
#           yield L[1:-1]
#           for i in range(len(L) - 1):
#               L.append(L.pop(0) + L[0])  # 弹出队首元素并将其与当前队首元素之和加入到队尾
#           L.append(0)  # 加个0，帮队列推一下屁股，凑成标准体位。
# n = 0
# for t in triangle():
#     print(t)
#     n = n + 1
#     if n == 10:
#         break
# T = [1, 2, 3, 4, 6]
# T.append(9)
# print T

# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     # return 'done'

# f = fib(10)
# # print('fib(10):', f)
# for x in f:
#     print(x)
# # call generator manually:
# g = fib(5)
# while 1:
#     try:
#         x = next(g)
#         print 'g:', x
#     except StopIteration as e:
#         print('Generator return value:', e.value)
#         break
