# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        fast_cursor = head
        slow_cursor = head
        while fast_cursor.next and fast_cursor.next.next:
            fast_cursor = fast_cursor.next.next
            slow_cursor = slow_cursor.next
            if fast_cursor == slow_cursor:
                return True
        return False
