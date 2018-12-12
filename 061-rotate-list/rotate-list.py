# Given a linked list, rotate the list to the right by k places, where k is non-negative.
#
# Example 1:
#
#
# Input: 1->2->3->4->5->NULL, k = 2
# Output: 4->5->1->2->3->NULL
# Explanation:
# rotate 1 steps to the right: 5->1->2->3->4->NULL
# rotate 2 steps to the right: 4->5->1->2->3->NULL
#
#
# Example 2:
#
#
# Input: 0->1->2->NULL, k = 4
# Output: 2->0->1->NULL
# Explanation:
# rotate 1 steps to the right: 2->0->1->NULL
# rotate 2 steps to the right: 1->2->0->NULL
# rotate 3 steps to the right: 0->1->2->NULL
# rotate 4 steps to the right: 2->0->1->NULL
#


'''
思路:利用队列的的数据结构
注意:最后一个元素要指向None 否则会出现环 检测代码输出为无限循环

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head==None or head.next==None or k==0:
            return head
        cnt = 0
        cur = head
        while(cur!=None):
            cur = cur.next
            cnt += 1
        if(k%cnt==0):
            return head
        cur = head
        cnt = cnt - k % cnt
        q1 = []
        q2 = []
        for i in range(cnt): #q1 长度
            q1.append(cur)
            cur = cur.next
        while(cur!=None):
            q2.append(cur)
            cur = cur.next
        head = q2.pop(0)
        cur = head
        
        
        for i in range(len(q2)):
            cur.next = q2[i]
            cur = cur.next
        
        
        for i in range(len(q1)):
            cur.next = q1[i]
            cur = cur.next
        cur.next = None
        return head
        
        
        
            
