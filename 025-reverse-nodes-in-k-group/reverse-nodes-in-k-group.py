# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
#
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
#
#
#
#
# Example:
#
# Given this linked list: 1->2->3->4->5
#
# For k = 2, you should return: 2->1->4->3->5
#
# For k = 3, you should return: 3->2->1->4->5
#
# Note:
#
#
# 	Only constant extra memory is allowed.
# 	You may not alter the values in the list's nodes, only nodes itself may be changed.
#
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        cur = head
        cnt = 0
        grp = 0
        while(cur!=None): #计算节点数目
            cur = cur.next
            cnt += 1
        if cnt<k:
            return head
        grp = cnt//k      #总共分成grp组
        
        queue = []
        cur = head
        while(grp>0): #遍历组 利用堆栈保存节点顺序
            tmpList = []
            for i in range(k): #遍历k
                tmpList.append(cur)
                cur = cur.next
            queue.append(tmpList[:])
            grp -= 1
        newHead = queue[0].pop() #新的头结点
        newcur = newHead
        while(len(queue)!=0):
            tmpgrp = queue.pop(0) #每一组出队列
            while(len(tmpgrp)!=0):
                newcur.next = tmpgrp.pop() #每一队列元素出栈
                newcur = newcur.next
        newcur.next = cur
        return newHead
                
        
        
