# Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
#
# This is case sensitive, for example "Aa" is not considered a palindrome here.
#
# Note:
# Assume the length of given string will not exceed 1,010.
#
#
# Example: 
#
# Input:
# "abccccdd"
#
# Output:
# 7
#
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.
#
#


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        _set = set(s)
        _list = list(s)
        tmp = 0
        odd = 0
        for item in _set:
            x = _list.count(item)
            if x//2>0:  # 2,3,4
                odd += int(_list.count(item)//2)*2
                if x%2 > 0:
                    tmp =1 
            else:
                tmp = 1
        return odd+tmp

