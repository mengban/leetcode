# Find the sum of all left leaves in a given binary tree.
#
# Example:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 层次遍历 left累加
        if not root:
            return 0
        queue = [root]
        _sum = 0
        while(len(queue)>0):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
                if not node.left.left and not node.left.right:  # 是叶子
                    _sum += node.left.val
            if node.right:
                queue.append(node.right)
        return _sum
            
        
