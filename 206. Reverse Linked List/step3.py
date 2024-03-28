# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cursor = head
        prev_node = None
        while cursor:
            tmp = cursor.next
            cursor.next = prev_node
            prev_node = cursor
            cursor = tmp
        return prev_node