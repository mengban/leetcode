# Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
#
# The same repeated number may be chosen from candidates unlimited number of times.
#
# Note:
#
#
# 	All numbers (including target) will be positive integers.
# 	The solution set must not contain duplicate combinations.
#
#
# Example 1:
#
#
# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
#   [7],
#   [2,2,3]
# ]
#
#
# Example 2:
#
#
# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]
#
#


'''
递归解法
'''
class Solution:
    
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        path = []
        self.ret = []
        if target in candidates:
            self.ret.append([target])
        for i in range(len(candidates)):
            self.func(candidates,target-candidates[i],path + [candidates[i]])
        tmp = [sorted(x) for x in self.ret]
        set_ret = []
        for item in tmp:
            #print(item)
            if item not in set_ret:
                set_ret.append(item)
        #print(set_ret)
        return set_ret

    def func(self ,candidates,target,path):
        if target <=0:
            return None
        if target in candidates:
            self.ret.append(path+[target])
        for i in range(len(candidates)):
            self.func(candidates,target-candidates[i],path+[candidates[i]])
        
            
