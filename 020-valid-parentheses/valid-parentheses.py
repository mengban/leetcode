# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
#
# 	Open brackets must be closed by the same type of brackets.
# 	Open brackets must be closed in the correct order.
#
#
# Note that an empty string is also considered valid.
#
# Example 1:
#
#
# Input: "()"
# Output: true
#
#
# Example 2:
#
#
# Input: "()[]{}"
# Output: true
#
#
# Example 3:
#
#
# Input: "(]"
# Output: false
#
#
# Example 4:
#
#
# Input: "([)]"
# Output: false
#
#
# Example 5:
#
#
# Input: "{[]}"
# Output: true
#
#


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 用数据结构栈 
        # 当时想到到数据结构课上的例题应用
        # 用数据结构栈 
        # 当时想到到数据结构课上的例题应用
        if not s:
            return True
        stack = []
        _dic = {"(":")","[":"]","{":"}"}
        for char in s:
            if char in _dic:  # ( [ { 进栈
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                if _dic[stack.pop()] != char:  # 出栈
                    return False
        if len(stack) == 0:
            return True
        else:
            return False 
            
            
            
        
        
