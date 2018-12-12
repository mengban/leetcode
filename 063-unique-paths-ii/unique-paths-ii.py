# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#
# Now consider if some obstacles are added to the grids. How many unique paths would there be?
#
#
#
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
#
# Note: m and n will be at most 100.
#
# Example 1:
#
#
# Input:
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# Output: 2
# Explanation:
# There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
#
#


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        mar = obstacleGrid[:]
        m = len(mar)
        n = len(mar[0])
        if mar[0][0]==1 or mar[m-1][n-1]==1:
            return 0
        if m==1 and n==1:
            return 1 if mar[0][0]==0 else 0
        
        if 1 not in mar[0]: #第一行没有障碍 说明全为0 改为1
            for i in range(n):
                mar[0][i] = 1
        else:
            for i in range(n): #1在 全部改为0
                if mar[0][i] ==1:
                    for j in range(i,n):
                        mar[0][j] =0
                    break
                    if i==n-1:
                        mar[0][i]=0
                mar[0][i] = 1
        tmp = []
        for i in range(m):#看第一列有没有1 修复[0,0]改为1的bug
            tmp.append(mar[i][0])
            
        if 1 not in tmp[1:]:  #[0,0]不计
            for i in range(m):
                mar[i][0] = 1
                #print('set 1')
        else:
            for i in range(1,m):  #还是[0,0] 的锅
                print('else',i,m)
                if mar[i][0] == 1:
                    for j in range(i,m):
                        mar[j][0] = 0
                    if i==m-1:
                        mar[i][0] = 0
                    break
                mar[i][0] = 1
                #print('set 1')
        print(mar)     
        for i in range(1,m):
            for j in range(1,n):
                if mar[i][j]==0:
                    mar[i][j] = mar[i-1][j] + mar[i][j-1]
                else:
                    mar[i][j] = 0
        #print(mar)
        return mar[m-1][n-1]
        
        
        
