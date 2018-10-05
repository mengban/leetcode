# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
#
# If the last word does not exist, return 0.
#
# Note: A word is defined as a character sequence consists of non-space characters only.
#
# Example:
#
# Input: "Hello World"
# Output: 5
#
#


class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = s.split(" ")
        while "" in ret:
            ret.remove("")
        if len(ret)== 0 :
            return 0
        else:
            return len(ret[-1])
        
        
