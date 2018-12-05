# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
#
# Example:
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
#
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None or l2 ==None:
            return l2 if l1 == None else l1#有链表为空
        head = None
        if l1.val>=l2.val: #最小值做头节点
            head = l2
            l2 = l2.next
        else:
            head = l1
            l1 = l1.next
        cur = head  #当前节点
        while l1!=None and l2!=None:
            if l1.val>=l2.val:
                cur.next = l2
                l2 = l2.next
            else:
                cur.next = l1
                l1 = l1.next
            cur = cur.next
        if l1==None:
            cur.next = l2
        else:
            cur.next = l1
        return head
        
        
        
