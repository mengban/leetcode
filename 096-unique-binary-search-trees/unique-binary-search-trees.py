# Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?
#
# Example:
#
#
# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
#
#


'''
规律题目:
1 2 3
[0]*[2]+[1]*[2]+[2]*[0]

1 2 3 4
[0]*[3]+[1]*[2]+[2]*[1]+[3]*[0]

1 2 3 4 5
[0]*[4]+[1]*[3]+[2]*[2]+[3]*[1]+[4]*[0]
'''
class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        _sum =7
        ret = 7
        table = []
        table.append(1) # 0
        table.append(1) # 1
        table.append(2) # 2
        table.append(5) # 3
        m = (n+1)//2
        for i in range(4,n+1): #3 的时候求的是第4个数的
            ret = 0
            if i%2 == 0: # 偶数
                for j in range(i//2):
                    ret += table[j]*table[i-1-j]
                ret *= 2 
            else:        #奇数
                for j in range(i//2):
                    ret += table[j]*table[i-1-j]
                ret *= 2
                ret += table[i//2]**2
            table.append(ret)
            
        return table[n]
