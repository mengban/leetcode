# Given a linked list, swap every two adjacent nodes and return its head.
#
# You may not modify the values in the list's nodes, only nodes itself may be changed.
#
#  
#
# Example:
#
#
# Given 1->2->3->4, you should return the list as 2->1->4->3.
#
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
利用栈数据结构 重新构造链表
'''
class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(head == None):
            return head
        if(head.next == None):
            return head
        nodeList = []
        node = head
        while(node!=None):
            nodeList.append(node)
            node = node.next
        if(len(nodeList)%2==0):#偶数个
            last = None
            while(len(nodeList)!=0):
                first = nodeList.pop()
                second = nodeList.pop()
                second.next = last
                first.next = second
                last = first
        else:#奇数个
            last = nodeList.pop()
            while(len(nodeList)!=0):
                first = nodeList.pop()
                second = nodeList.pop()
                second.next = last
                first.next = second
                last = first
        return first
            
            
            
        
