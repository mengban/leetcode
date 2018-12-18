# Given preorder and inorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.
#
# For example, given
#
#
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
#
# Return the following binary tree:
#
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
递归思路求解 很耗时
不过肯定有非递归思路 可以思考一下
'''

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        #print(preorder)
        if len(preorder)==0:
            return None
        if(len(preorder)==1):
            node = TreeNode(preorder[0])
            return node
        root = preorder[0]
        posinorder = inorder.index(root) #root 中序位置
        left = posinorder #左节点数目
        root = TreeNode(root)
        root.left = self.buildTree(preorder[1:left+1],inorder[0:left])
        root.right = self.buildTree(preorder[left+1:],inorder[left+1:])
        return root
