# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head        
        current_node = head
        next_node = head.next
        current_node.next = None
        while next_node:
            next_next_node = next_node.next
            next_node.next = current_node
            current_node = next_node
            next_node = next_next_node
        return current_node