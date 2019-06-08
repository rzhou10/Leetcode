'''
    Middle of the Linked List
    Runtime: 36 ms
'''

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head.next:
            return head
        
        vals = []
        length = 1
        
        while head.next:
            head = head.next
            length += 1
            vals.append(head)
        vals.append(head)
        
        return vals[int(length / 2) - 1]