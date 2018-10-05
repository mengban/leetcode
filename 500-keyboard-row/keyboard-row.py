# Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below. 
#
#
#
#
#
#
#
# Example 1:
#
# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]
#
#
#
# Note:
#
# You may use one character in the keyboard more than once.
# You may assume the input string will only contain letters of alphabet.
#
#


class Solution:
    def isubstring(self,word):
        top = "qwertyuiop]QWERTYUIOP"
        bottom = "asdfghjklASDFGHJKL"
        down = "zxcvbnmZXCVBNM"
        if word[0] in top:
            for char in word:
                if char not in top:
                    return False
        if word[0] in bottom:
            for char in word:
                if char not in bottom:
                    return False
        if word[0] in down:
            for char in word:
                if char not in down:
                    return False
        return True
    def findWords(self,words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ret = []
        for item in words:
            #print('item',item,type(item))
            if self.isubstring(item)==True:
                ret.append(item)
        return ret

                
        
                
                    
            
        
