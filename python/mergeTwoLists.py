"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        result = ListNode()
        temp = result
        print(result,temp)
        while l1 != None and l2 != None: 
            # print(result)
            # print(temp)
            if l1.val < l2.val: 
                temp.next = l1 
                l1 = l1.next 
            else: 
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        
        if(l1):
            temp.next = l1
        elif(l2):
            temp.next = l2
        
#         result = result.next
        
        return result.next
