# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
#
# Example 1:
#
#
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
#
#
# Example 2:
#
# Input:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
#


class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return []
        ret = []
        row = len(matrix)
        clo = len(matrix[0])
        circleCnt = min((row+1)//2,(clo+1)//2)
        breakr = row//2
        breakc = clo//2
        prerow = 0
        preclo = 0
        for _ in range (circleCnt): #圈数的循环 从0开始
            for i in range(_,clo-_):  #-> (圈数循环 列数-圈数循环)行不变 列变
                ret.append(matrix[_][i])
            prerow = _
            
            for i in range(_+1,row-_):  # |>(圈数循环+1 行数-圈数循环） 行变 列不变
                ret.append(matrix[i][clo-_-1])
            preclo = clo-_-1
            
            if(row-_-1>_):
                for i in range(_,clo-1-_):  #(圈数循环 列数-1-圈数循环)
                    ret.append(matrix[row-_-1][clo-2-i]) #行不变 列变
            prerow = row-_-1
            if(clo-_-1>_):
                for i in range(_+1,row-1-_):  #(圈数循环+1 行数-1-圈数循环)
                    ret.append(matrix[row-1-i][_])  #行变 列不变
            preclo = _
            
                
        return ret
            
        
