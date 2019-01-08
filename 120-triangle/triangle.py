# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
#
# For example, given the following triangle
#
#
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
#
#
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
#
# Note:
#
# Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
#


class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle) == 0:
            return 0
        _sum = triangle[-1][:] #等于最后一行
        #print(_sum)
        m = len(triangle)
        for i in range(-2,-m-1,-1):
            for j in range(len(triangle[i])):
                _sum[j] = min(_sum[j],_sum[j+1]) + triangle[i][j]
        return _sum[0]
        
        
