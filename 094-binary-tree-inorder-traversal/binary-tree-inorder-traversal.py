# Given a binary tree, return the inorder traversal of its nodes' values.
#
# Example:
#
#
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# Output: [1,3,2]
#
# Follow up: Recursive solution is trivial, could you do it iteratively?
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        ret = []
        if root == None:
            return ret
        while(len(stack)!=0 or root!=None):
            while(root!=None): #左子树全部进栈
                stack.append(root)
                root = root.left
            if(len(stack)!=0):
                root = stack.pop()
                ret.append(root.val)
                root = root.right
        return ret

