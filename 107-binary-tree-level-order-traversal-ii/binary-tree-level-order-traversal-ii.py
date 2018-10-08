# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
#
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
#
#
# return its bottom-up level order traversal as:
#
# [
#   [15,7],
#   [9,20],
#   [3]
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
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [root]
        ret = []
        tmp = []
        while(len(queue)>0):
            i = 0
            length = len(queue)
            while i<length:
                node = queue.pop(0)
                tmp.append(node.val)
                if  node.left:
                    queue.append(node.left)
                if  node.right:
                    queue.append(node.right)
                i += 1
            ret.append(tmp)
            tmp=[]
        return ret[::-1]
                
            
        
