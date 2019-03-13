# _*_ coding:utf-8 _*_
# @Author: Bie
# @Time: 2018年10月29日

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romanDict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        result = 0
        result_list = []
        while len(s) > 0:
            if len(s) == 1:
                result_list.append(s[0])
                s = ''
            elif romanDict[s[0]] <romanDict[s[1]]:
                result_list.append(s[:2])
                s = s[2:]
            else:
                result_list.append(s[0])
                s = s[1:]
        for i in result_list:
            result += romanDict[i]
        print(result)
        return result

sol = Solution()
sol.romanToInt('IV')