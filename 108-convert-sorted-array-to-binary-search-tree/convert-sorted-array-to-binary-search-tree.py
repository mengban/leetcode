# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
#
# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
#
# Example:
#
#
# Given the sorted array: [-10,-3,0,5,9],
#
# One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
#
#       0
#      / \
#    -3   9
#    /   /
#  -10  5
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # 利用递归
        # 平衡二叉树
        # 搜索树
        if not nums:
            return None
        mid = len(nums)//2
        root = TreeNode(nums[mid])
        l = nums[:mid]
        r = nums[mid+1:]
        root.left = self.sortedArrayToBST(l)
        root.right = self.sortedArrayToBST(r)
        return root
        
        
