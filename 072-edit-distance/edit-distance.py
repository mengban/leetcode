# Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.
#
# You have the following 3 operations permitted on a word:
#
#
# 	Insert a character
# 	Delete a character
# 	Replace a character
#
#
# Example 1:
#
#
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
#
#
# Example 2:
#
#
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')
#
#


'''
递归过于暴力...
if len(word1) == 0:
    return len(word2)
elif len(word2)  == 0:
    return len(word1)
elif word1[-1] == word2[-1]: #最后一位相等
    return self.minDistance(word1[:-1],word2[:-1])
else:
    return min(self.minDistance(word1[:-1],word2[:])+1,self.minDistance(word1[:],word2[:-1])+1,
               self.minDistance(word1[:-1],word2[:-1])+1)

非递归:以fab fxy 为例.填满表格即可
      f a b
    0 1 2 3
  0 0 1 2 3
f 1 1 0
x 2 2 
y 3 3
'''
class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        lena = len(word1)
        lenb = len(word2)
        dis = [[i for i in range(lena+1)] for j in range(lenb+1)]  #lenb+1 行 lena+1列
        for i in range(lena+1): #填充第一行
            dis[0][i] = i
        for i in range(lenb+1): #填充第一列
            dis[i][0] = i
        #print(dis)
        for i in range(lenb):  # 这么多行
            for j in range(lena): # 这么多列
                if word1[j] == word2[i]:
                    dis[i+1][j+1] = dis[i][j]
                else:
                    dis[i+1][j+1] = min(dis[i][j+1]+1,dis[i+1][j]+1,dis[i][j]+1)
        '''
        for i in range(min(lena,lenb)):  #索引ab 长度开始 更新dis需要偏移加1
            if word1[i] == word2[i]:
                dis[i+1][i+1] = dis[i][i] #
            else:
                dis[i+1][i+1] = min(dis[i-1][i]+1,dis[i][i-1]+1,dis[i][i]+1) #更新对角线
            for j in range(i,lena-1):#更新行
                dis[i+1][j+1+1] = dis[i+1][j+1] + 1
                
            for j in range(i,lenb-1):#更新列
                dis[j+1+1][i+1] = dis[j+1][i+1] + 1
        '''
        return dis[lenb][lena]
