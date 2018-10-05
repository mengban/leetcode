#
# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
#
# Examples:
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.
#
#
#
#
# Note: You may assume the string contain only lowercase letters.
#


class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        letter = "abcdefghijklmnopqrstuvwxyz"
        index = []
        for item in letter:
            if s.count(item) == 1:
                index.append(s.index(item))
        return min(index) if len(index) > 0 else  -1
                

                        
