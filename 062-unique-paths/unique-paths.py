# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#
# How many possible unique paths are there?
#
#
# Above is a 7 x 3 grid. How many possible unique paths are there?
#
# Note: m and n will be at most 100.
#
# Example 1:
#
#
# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right
#
#
# Example 2:
#
#
# Input: m = 7, n = 3
# Output: 28
#


'''
思路1:递归 f(m,n)=f(m-1,n)+f(m,n-1) 很不幸  超时
思路2:建立一个矩阵 从对角加起
1 1 1
1 2 3
1 3 6
'''
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        mar = [[0 for i in range(n)] for j in range(m)]
        print(len(mar))
        
        for i in range(n):#每一列第一个为1
            mar[0][i] = 1
        for i in range(m):#没一行 第一个为1
            mar[i][0] = 1
        for i in range(1,m): #从第二行开始
            for j in range(1,n):#从第二列开始
                mar[i][j] = mar[i][j-1]+mar[i-1][j]
        return mar[m-1][n-1]
        #print(mar)
