# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as:
#
#
# a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
#
#
# Example 1:
#
# Given the following tree [3,9,20,null,null,15,7]:
#
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# Return true.
#
# Example 2:
#
# Given the following tree [1,2,2,3,3,null,null,4,4]:
#
#
#        1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
#
#
# Return false.
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 每个节点都是平衡二叉树
        # 左子树与右子树深度差不大于1
        # 广度优先遍历所有node 查看abs
        if not root:      # 空 返回True
            return True
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if abs(self.depth(node.left)-self.depth(node.right))>1:   #遍历每一个node 判断其左右子树深度
                return False
        return True
        
    def depth(self,tree):
        if not tree:  # 节点为空 直接返回0
            return 0
        return max(self.depth(tree.left),self.depth(tree.right))+1
       
        
