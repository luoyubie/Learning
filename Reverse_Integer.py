# _*_ coding:utf-8 _*_
# @Author: Bie
# @Time: 2018年10月28日

# 整数反转
def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    i = 0
    a= []
    while x <= -1:
        a.append(-(-x%10))
        x = -(-x//10)
        i += 1
    while x > 0:
        a.append(x%10)
        x = x//10
        i += 1
    xr = 0
    for j in range(i):
        xr += a[-1] * 10 ** j
        a.pop(-1)
    if xr < -2**31 or xr > 2**31-1:
        return 0
    else:
        return xr


x = -42949
print(reverse(x))



