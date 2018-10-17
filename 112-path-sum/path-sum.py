# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
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
#  /  \      \
# 7    2      1
#
#
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        # 递归解法 对于root节点 从左右子树找出和为 sum-root.val的即可
        
        if not root:  # 空节点
            return False
        if not root.left and not root.right: # 叶子节点 
            if sum == root.val:
                return True
            else:
                return False
        # 返回值取 or 有一true即可
        return self.hasPathSum(root.left,sum - root.val) or self.hasPathSum(root.right,sum - root.val)
        
        
