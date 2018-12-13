# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
#
#
# 	Integers in each row are sorted from left to right.
# 	The first integer of each row is greater than the last integer of the previous row.
#
#
# Example 1:
#
#
# Input:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 3
# Output: true
#
#
# Example 2:
#
#
# Input:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 13
# Output: false
#


'''
思路：从右上出发 先确定行 再确定列
'''
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m==0 :
            return False
        n = len(matrix[0])
        if n==0:
            return False
            

        x = 0
        y = n-1
        
        while(x<m and matrix[x][y]<=target): 
            if matrix[x][y] == target:
                return True
            x += 1
        if x == m:  #已经过届了
            return False
        while(matrix[x][y]>=target and y>=0):
            if matrix[x][y] == target:
                return True
            y -= 1
            
        return False
            
        
