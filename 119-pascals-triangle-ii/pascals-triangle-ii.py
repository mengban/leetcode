# Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
#
# Note that the row index starts from 0.
#
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it.
#
# Example:
#
#
# Input: 3
# Output: [1,3,3,1]
#
#
# Follow up:
#
# Could you optimize your algorithm to use only O(k) extra space?
#


class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ret = []
        for i in range (rowIndex+1):
            ret.append([0]*(i+1))   
            for j in range(i+1):
                if j==0 or j==i:
                    ret[i][0] = 1
                    ret[i][i-j] = 1
                if j< i:
                    ret[i][j] = ret[i-1][j-1]+ret[i-1][j]
        return ret[rowIndex]  
        
