# _*_ coding:utf-8 _*_
# @Author: Bie
# @Time: 2018年10月26日

# 221. 最大正方形
# 在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积
# mat = [['1','0',"1",'0','0'],['1','0','1','1','1'],['1','1','1','1','1'],['1','0','1','1','1']]
mat = [['0','0'],['0','0']]
def maximalSquare(matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    if len(matrix) == 0:
        return 0
    elif len(matrix) ==1 and '1' in matrix[0]:
        return 1
    elif ['1'] in matrix:
        return 1
    row = len(matrix)
    col = len(matrix[0])
    rm = [[0]*col for i in range(row)]
    for i in range(row):
        rm[i][0] = int(matrix[i][0])
    for i in range(col):
        rm[0][i] = int(matrix[0][i])
    for i in range(1,row):
        for j in range(1,col):
            rm[i][j] = int(matrix[i][j])
            if rm[i][j] != 0:
                rm[i][j] = min(rm[i][j-1],rm[i-1][j],rm[i-1][j-1]) + 1

    r = 0
    for i in rm:
        for j in i:
            if r<j:
                r = j
    return r** 2

print(maximalSquare(mat))




