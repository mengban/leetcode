# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#
#
#
# But the following [1,2,2,null,3,null,3]  is not:
#
#     1
#    / \
#   2   2
#    \   \
#    3    3
#
#
#
#
# Note:
# Bonus points if you could solve it both recursively and iteratively.
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 树的对称和树的same思路是一样的 
# 就是遍历顺序不一样而已
# 对称：左节点==右节点
# 相等：右节点==左节点
class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self._isSy(root.left,root.right)
        
    def _isSy(self,p,q):
        if p and q:
            return p.val ==q.val and self._isSy(p.left,q.right) and self._isSy(p.right,q.left)
        return p==q
    
        
        
        
        
        
        
