# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def _search_catchup_node(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast_cursor = head
        slow_cursor = head
        while fast_cursor and fast_cursor.next:
            fast_cursor = fast_cursor.next.next
            slow_cursor = slow_cursor.next
            if fast_cursor == slow_cursor:
                return fast_cursor
        return None

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        catchup_node = self._search_catchup_node(head)
        if not catchup_node:
            return None
        from_start = head
        from_catchup = catchup_node
        while from_start != from_catchup:
            from_start = from_start.next
            from_catchup = from_catchup.next
        return from_start
