# Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
#
# Example:
#
#
# Input: 3
# Output:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]
#
#


'''
上一道题稍微改一下就好了
'''
class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0 for i in range(n)] for i in range(n)]
        row = n
        clo = n
        circleCnt = min((row+1)//2,(clo+1)//2)
        breakr = row//2
        breakc = clo//2
        prerow = 0
        preclo = 0
        cnt = 1
        for _ in range (circleCnt): #圈数的循环 从0开始
            for i in range(_,clo-_):  #-> (圈数循环 列数-圈数循环)行不变 列变
                matrix[_][i] = cnt
                cnt += 1
            prerow = _
            
            for i in range(_+1,row-_):  # |>(圈数循环+1 行数-圈数循环） 行变 列不变
                matrix[i][clo-_-1] = cnt
                cnt += 1
            preclo = clo-_-1
            
            if(row-_-1>_):  #加入边界检测条件
                for i in range(_,clo-1-_):  #(圈数循环 列数-1-圈数循环)
                    matrix[row-_-1][clo-2-i] = cnt #行不变 列变
                    cnt += 1
            prerow = row-_-1
            if(clo-_-1>_): #加入边界检测条件
                for i in range(_+1,row-1-_):  #(圈数循环+1 行数-1-圈数循环)
                    matrix[row-1-i][_] = cnt  #行变 列不变
                    cnt += 1
            preclo = _        
        return matrix
        
