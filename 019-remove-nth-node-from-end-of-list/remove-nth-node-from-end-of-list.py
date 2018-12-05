# Given a linked list, remove the n-th node from the end of list and return its head.
#
# Example:
#
#
# Given linked list: 1->2->3->4->5, and n = 2.
#
# After removing the second node from the end, the linked list becomes 1->2->3->5.
#
#
# Note:
#
# Given n will always be valid.
#
# Follow up:
#
# Could you do this in one pass?
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if(head==None):
            return None
        cur = head
        cnt = 0
        while(cur!=None):
            cur = cur.next;
            cnt += 1
        if(n==cnt):  #删除头结点
            return head.next
        cur = head
        while(cnt-n-1>0):
            cnt -= 1
            cur = cur.next
        cur.next = cur.next.next
        
        return head
            
        
