# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def _get_collision_node(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast_cursor = head
        slow_cursor = head
        while fast_cursor and fast_cursor.next:
            fast_cursor = fast_cursor.next.next
            slow_cursor = slow_cursor.next
            if fast_cursor == slow_cursor:
                return fast_cursor
        return None

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        collision_node = self._get_collision_node(head)
        if not collision_node:
            return None
        head_cursor = head
        collision_cursor = collision_node
        while head_cursor != collision_cursor:
            head_cursor = head_cursor.next
            collision_cursor = collision_cursor.next
        return head_cursor
