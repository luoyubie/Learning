# _*_ coding:utf-8 _*_
# @Author: Bie
# @Time: 2019年05月20日


# python反射机制 -- 文件内通过字符串调用函数
import sys
moudle = sys.modules[__name__]
fun1 = getattr(moudle,'文件内的函数名')

# python反射机制 从其他模块通过 函数名(string)调用函数
md = __import__("模块名",fromlist=True)
fun2 = getattr(md,"函数名")


