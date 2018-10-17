# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given the below binary tree and sum = 22,
#
#
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \    / \
# 7    2  5   1
#
#
# Return:
#
#
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        self.ans=[]
        self.dfs(root,[root.val],sum)
        #print(self.ans)
        return self.ans
    def dfs(self,root,path,_sum):
        if not root: # 空节点
            return []
        #path.append(root.val)
       
        if not root.left and not root.right: # 叶子节点
           
            if sum(path) == _sum: 
                #print(path)
                self.ans.append(path)
        if root.left:
            self.dfs(root.left,path+[root.left.val],_sum)
        if root.right:
            self.dfs(root.right,path+[root.right.val],_sum)
        
            
        
