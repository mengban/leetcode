# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
#
#
#
# Example:
#
#
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
#
#
# Note:
#
# Although the above answer is in lexicographical order, your answer could be in any order you want.
#


'''
采用备忘录法
递归太耗时
'''
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        num_letter = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        if(len(digits)==0):
            return []
        preList = []
        retList = []
        
        for item in num_letter[digits[0]]:
            preList.append(item)
        if(len(digits)==1):
            return preList
        for i in range(1,len(digits)):
            #print('for i in range',i)
            retList = []
            for item in preList:
                #print('for item in prelist',preList)
                for item2 in num_letter[digits[i]]:
                    retList.append(item+item2)
                    #print('for item2 in prelist',preList)
            preList = retList[:]
            
            #print(retList)
        return retList

        
