# _*_ coding:utf-8 _*_
# @Author: Bie
# @Time: 2019年03月12日

def fib(max):
    n,a,b = 0,0,1
    while n<max:
        yield b
        a,b = b,a+b
        n += 1
    return 'done'

for i in fib(10):
    print(i)

