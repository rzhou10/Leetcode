'''
    Reverse Linked List
    Runtime: 20 ms
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        current = head
        
        while current != None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        
        return prev