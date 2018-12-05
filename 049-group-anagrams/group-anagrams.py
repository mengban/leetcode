# Given an array of strings, group anagrams together.
#
# Example:
#
#
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
#
# Note:
#
#
# 	All inputs will be in lowercase.
# 	The order of your output does not matter.
#
#


'''
思路：排序
然后hash化 {字符串:[脚标1,脚标2]}
'''
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sortedstr = [sorted(item) for item in strs]
        sortedstr = [''.join(item) for item in sortedstr]
        #print(sortedstr)
        hashstr = {}
        for i in range(len(sortedstr)):
            item = sortedstr[i]
            if item not in hashstr.keys():
                hashstr[item] = [i]
            else:
                hashstr[item] = hashstr[item] +[i]
        #print(hashstr)
        ret = []
        for index in hashstr.values():
            tmp = []
            #print(index)
            for pos in index:
                tmp.append(strs[pos])
            ret.append(tmp[:])
        return ret
        
