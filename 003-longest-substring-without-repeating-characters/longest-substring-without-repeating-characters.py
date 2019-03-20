# Given a string, find the length of the longest substring without repeating characters.
#
#
# Example 1:
#
#
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
#
#
#
# Example 2:
#
#
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
#
#
# Example 3:
#
#
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
#
#
#
#


'''
滑动窗口遍历
'''
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=="":
            return 0
        start = 0
        end = 0
        maxLength = 0
        tmpList = []
        for item in s:
            end += 1
            if item in tmpList:
                start = tmpList.index(item) + 1
            tmpList = tmpList[start:]  #当前list排除重复
            start = 0 # start 置0
            tmpList.append(item)
            if(maxLength<len(tmpList)):
                maxLength = len(tmpList)
            #print(tmpList)
        return (maxLength)
        
