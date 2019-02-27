# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
#
# You may not modify the values in the list's nodes, only nodes itself may be changed.
#
# Example 1:
#
#
# Given 1->2->3->4, reorder it to 1->4->2->3.
#
# Example 2:
#
#
# Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
#
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head == None or head.next==None or head.next.next==None: # 有0 1 2 
            pass
        else:
            print('haha')
            q = []
            cur = head
            
            while cur != None:
                #print(cur.val)
                q.append(cur)
                cur = cur.next
            cur = q.pop(0)
            flag = True
            
            while len(q)>0:
                #print(flag,len(q))
                if flag == True:
                    cur.next = q.pop()
                    flag = False
                else:
                    cur.next = q.pop(0)
                    flag = True
                cur = cur.next
            cur.next = None

        
        
        
        
        
        
