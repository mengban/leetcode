# Given a binary tree, return the postorder traversal of its nodes' values.
#
# Example:
#
#
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# Output: [3,2,1]
#
#
# Follow up: Recursive solution is trivial, could you do it iteratively?
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
前序遍历最好写 直接通过进出栈操作
后序遍历是前序遍历的倒叙
'''
class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        q = [root]
        path = []
        while len(q)>0:
            node = q.pop()
            path.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return path[::-1]
                
        
        
