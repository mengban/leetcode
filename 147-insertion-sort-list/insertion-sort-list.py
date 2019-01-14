# Sort a linked list using insertion sort.
#
#
#
#
#
# A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
# With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list
#  
#
#
#
#
# Algorithm of Insertion Sort:
#
#
# 	Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
# 	At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
# 	It repeats until no input elements remain.
#
#
#
# Example 1:
#
#
# Input: 4->2->1->3
# Output: 1->2->3->4
#
#
# Example 2:
#
#
# Input: -1->5->3->4->0
# Output: -1->0->3->4->5
#
#


'''
这道题目深刻的暴露了自己在编程时的毛病
- 1.对于边界条件不敏感
  这是大忌啊。对于不确定的边界条件 直接写了过去 急于求成
- 2.没想好便下笔
  以后应该在草稿纸上把思路想清楚 遇到的可能情况搞明白再下笔.不然来回改bug 实在是太惨了

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        cur = head
        nodes = []
        while cur!=None: #遍历得到所有node
            nodes.append(cur)
            cur = cur.next
        for i in range(1,len(nodes)):
            for j in reversed(range(i)):
                if nodes[j].val <= nodes[i].val and j >=0: #找到这个位置了 位置索引为j+1
                    #print('if',i,j)
                    pos = i
                    while pos > j+1:
                        tmp = nodes[pos]
                        nodes[pos] = nodes[pos - 1] 
                        nodes[pos - 1] = tmp
                        pos -= 1
                    break   #找到之后break
                elif nodes[j].val >= nodes[i].val and j ==0 : #最小值应该放在开头
                    pos = i
                    #print('else',j)
                    while pos > j:
                        tmp = nodes[pos]
                        nodes[pos] = nodes[pos - 1] 
                        nodes[pos - 1] = tmp
                        pos -= 1
                    #print([x.val for x in nodes])
                    
        head = nodes.pop(0)
        cur = head
        #print(nodes)
        
        for i in range(len(nodes)):
            cur.next = nodes[i]
            cur = cur.next
        cur.next = None
        return head
            
        
