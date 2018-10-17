# Invert a binary tree.
#
# Example:
#
# Input:
#
#
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
#
# Output:
#
#
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
#
# Trivia:
# This problem was inspired by this original tweet by Max Howell:
#
# Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        #遍历 只要不是叶子节点就进行翻转
        if not root:
            return root
        queue = [root]
        while(len(queue)>0):
            node = queue.pop(0)
            if node.left or node.right: # 只要有左右节点
                tmp = node.left
                node.left = node.right
                node.right=tmp      
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return root
            
            
