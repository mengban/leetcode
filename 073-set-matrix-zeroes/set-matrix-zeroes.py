# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
#
# Example 1:
#
#
# Input: 
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# Output: 
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]
#
#
# Example 2:
#
#
# Input: 
# [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]
# Output: 
# [
#   [0,0,0,0],
#   [0,4,5,0],
#   [0,3,1,0]
# ]
#
#
# Follow up:
#
#
# 	A straight forward solution using O(mn) space is probably a bad idea.
# 	A simple improvement uses O(m + n) space, but still not the best solution.
# 	Could you devise a constant space solution?
#
#


class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        is0 = [[],[]]
        for i in range(m): #遍历每一行
            for j in range(n):#遍历每一列
                if matrix[i][j]==0: 
                    is0[0].append(i)
                    is0[1].append(j)
        for row in set(is0[0]):
            for col in range(n):
                matrix[row][col] = 0
        for col in set(is0[1]):
            for row in range(m):
                matrix[row][col] = 0
        
        
