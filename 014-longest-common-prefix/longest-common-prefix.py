# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
#
# Input: ["flower","flow","flight"]
# Output: "fl"
#
#
# Example 2:
#
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
#
# Note:
#
# All given inputs are in lowercase letters a-z.
#


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ""
        if len(strs)==1:
            return strs[0]  #1个元素 则返回该元素
        strSum = ""
        for i in range(len(strs[0])+1):  #i 最大值为len-1
            for item in strs:
                if(i>len(item)-1): #终止内圈循环  单词的循环
                    return strs[0][:i]
                strSum += item[i]  
                #print(strSum)
            #print(strSum)
            if len(set(strSum))!=1: # 前缀不同 说明到此已经不是共同前缀了
                return strs[0][:i]
            strSum = ""
        '''
        if len(set(strSum))!=1:
            return strs[0][:pos+1]  # break结束
        else:
            return strs[0][:pos+1]  #循环结束
        '''
            
        
