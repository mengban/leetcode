# Given a binary tree, flatten it to a linked list in-place.
#
# For example, given the following tree:
#
#
#     1
#    / \
#   2   5
#  / \   \
# 3   4   6
#
#
# The flattened tree should look like:
#
#
# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    pre_node = None
    last_node = None
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        #print('.')
        '''
        if root is None:
            return
        
        if self.last_node is not None:
            self.last_node.left = None
            self.last_node.right = root
            
        self.last_node = root
        right = root.right
        self.flatten(root.left)
        self.flatten(right)
        '''
        
        if root is None:
            return 
        if self.pre_node != None:
            self.pre_node.left = None
            self.pre_node.right = root
            
        self.pre_node = root
        right = root.right
        self.flatten(root.left)
        self.flatten(right)
