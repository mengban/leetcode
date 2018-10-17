# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
#
# Example 1:
#
#
# Input: 1->2->3->3->4->4->5
# Output: 1->2->5
#
#
# Example 2:
#
#
# Input: 1->1->1->2->3
# Output: 2->3
#
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        cur = head
        pre = ListNode(-1)
        ret = None
        pre.next = head  # 就让pre.next等于头节点
        Flag = False
        same_value = None
        while(cur): #当前节点不为空
            if not ret and pre:
                ret = pre
            if(cur.next):#当前节点下一节点存在
                if(cur.val == cur.next.val): # 相等
                    same_value = cur.val
                    flag = True
                    while(cur.next and cur.next.val==same_value ): # 当前节点下一节点存在 并且下一节点的值等于需要删除掉的值
                        #pre = cur 
                        cur = cur.next   #删除当前节点
                    
                    #跳出while 要么当前节点为末节点 要么当前值下一节点 不为same_value
                    if not cur.next: #末节点
                        pre.next = None # 末节点一定为same删除 删除掉该节点
                    else: # 不是末节点 cur.next.val 不为same
                        cur = cur.next  #删除该节点
                        pre.next = cur   
                else: # 不等
                    pre = cur  #迭代
                    cur = cur.next
                    
            else:
                return ret.next   
        return ret.next
                
        
        
