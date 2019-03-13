# _*_ coding:utf-8 _*_
# @Author: Bie
# @Time: 2018年10月31日

import time
"""
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。
"""
class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        stime = time.time()
        if abs(dividend) < abs(divisor):
            return 0
        if dividend == 0:
            return 0
        i = 0
        if (dividend>0 and divisor<0) or (dividend<0 and divisor>0):
            i = -len(range(abs(divisor),abs(dividend)+1,abs(divisor)))
        elif (dividend>0 and divisor>0) or (dividend<0 and divisor<0):
            i = len(range(abs(divisor), abs(dividend)+1, abs(divisor)))
        etime = time.time()
        print(etime-stime)
        if i > 2**31 -1 or i < -2**31:
            return 2**31 -1
        else:
            return i

sol = Solution()
print(sol.divide(1,1))
