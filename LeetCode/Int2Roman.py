# _*_ coding:utf-8 _*_
# @Author: Bie
# @Time: 2018年10月31日

class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        integer_Dict = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X',
                        9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        integer = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        result_list = []
        for i in integer:
            while num >= i:
                result_list.append(integer_Dict[i])
                num -= i
        result = ''.join(result_list)
        return result

sol = Solution()
print(sol.intToRoman(4))
