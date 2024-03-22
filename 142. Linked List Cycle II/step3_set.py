# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen_nodes = set()
        cursor = head
        while cursor:
            if cursor in seen_nodes:
                return cursor
            seen_nodes.add(cursor)
            cursor = cursor.next
        return None