# Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.
#
# Please note that the string does not contain any non-printable characters.
#
# Example:
#
# Input: "Hello, my name is John"
# Output: 5
#
#


class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 利用空格将字符串切分 统计切分结果
        if len(s)==0:
            return 0
        splited = s.split(" ")
        
        return (len(splited)-splited.count(''))
        
