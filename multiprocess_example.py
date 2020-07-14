# _*_ coding:utf-8 _*_
# @Author: Bie
# @Time: 2020年07月14日

import multiprocessing as mp
import time

num_cups = mp.cpu_count()


def ceshi(a, b):
    for i in range(100000000):
        a + b
    print(a + b)
    return a + b


def main1():
    # 串行测试时间36.4 s
    t0 = time.time()
    a_list = [1, 2, 3, 4, 5, 6, 7, 8]
    b_list = [1, 2, 3, 4, 5, 6, 7, 8]
    for a, b in zip(a_list, b_list):
        r = ceshi(a, b)
        print(r)
    t1 = time.time()
    print(t1 - t0)


def main2():
    # 多进程测试 8核10.9s 4核14.9s
    # 要在__name__ == "__main__"中运行多进程的代码
    t0 = time.time()
    a_list = [1, 2, 3, 4, 5, 6, 7, 8]
    b_list = [1, 2, 3, 4, 5, 6, 7, 8]
    with mp.Pool(num_cups - 4) as p:
        p.starmap(ceshi, zip(a_list, b_list))
    t1 = time.time()
    print(t1 - t0)


if __name__ == "__main__":
    main2()
