# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
#
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it.
#
# Example:
#
#
# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
#
#


class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ret = []
        for i in range (numRows):
            ret.append([0]*(i+1))   
            for j in range(i+1):
                if j==0 or j==i:
                    ret[i][0] = 1
                    ret[i][i-j] = 1
                if j< i:
                    ret[i][j] = ret[i-1][j-1]+ret[i-1][j]
        return ret       
