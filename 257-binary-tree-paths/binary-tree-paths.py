# Given a binary tree, return all root-to-leaf paths.
#
# Note: A leaf is a node with no children.
#
# Example:
#
#
# Input:
#
#    1
#  /   \
# 2     3
#  \
#   5
#
# Output: ["1->2->5", "1->3"]
#
# Explanation: All root-to-leaf paths are: 1->2->5, 1->3
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        # DFS + 栈结构
        self.stack = []
        self.ret = []
        if not root:
            return []
        self.dfs(root)
        _ret = []
        tmp = ""
        for item in self.ret:
            #print('*'*6)
            #print(item)
            for i in range(len(item)) :
                tmp = tmp+str(item[i])
                if i < len(item) -1:
                    tmp = tmp+"->"
            #print(tmp)
            _ret.append(tmp)
            tmp = ""
        #print(ret) 
        self.ret = []
        self.stack = []
        return _ret
       
    def dfs(self,node):
        if  node: # 不是空节点
            self.stack.append(node.val)
            if not node.left and not node.right:# 叶子节点
                #print(self.stack)
                self.ret.append(self.stack[:])
                #self.stack.pop()
                #print('叶子节点',node.val)
            #print(node.val)
            self.dfs(node.left)            
            self.dfs(node.right)
            self.stack.pop()
                
        
