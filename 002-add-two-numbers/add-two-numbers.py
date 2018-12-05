# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example:
#
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
#
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode    
        """
        if l1 == None or l2 == None:
            return l1 if l2==None else l1
        list1 = []
        list2 = []
        while(l1!=None):
            list1.append(l1.val)
            l1 = l1.next
        #list1 = list1[::-1]
        while(l2!=None):
            list2.append(l2.val)
            l2 = l2.next
        #list2 = list2[::-1]
        print(list1,list2)
        Interger1 = 0
        Interger2 = 0
        for i in range(len(list1)):
            Interger1 += list1[i]*(10**i)
            
        for i in range(len(list2)):
            Interger2 += list2[i]*(10**i)
        
        sum_ = Interger1 + Interger2
        head = ListNode(0)
        headtmp = head
        for item in list(str(sum_))[::-1]:
            head.next = ListNode(int(item))
            head = head.next
        
        return headtmp.next
