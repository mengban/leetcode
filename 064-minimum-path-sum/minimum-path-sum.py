# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.
#
# Example:
#
#
# Input:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.
#
#


class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n =len(grid[0])
        for i in range(1,n): #更新第一行所有
            grid[0][i] += grid[0][i-1] 
        for i in range(1,m):#更新第一列所有
            grid[i][0] += grid[i-1][0]
            
        for i in range(1,m):#第二行开始
            for j in range(1,n):#第二列开始
                if grid[i][j-1] > grid[i-1][j]:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += grid[i][j-1]
        return grid[m-1][n-1]
