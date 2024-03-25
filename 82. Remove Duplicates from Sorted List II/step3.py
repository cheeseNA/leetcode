# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def _skip_nodes_with_value(self, cursor: Optional[ListNode], skip_value: int) -> Optional[ListNode]:
        while cursor and cursor.val == skip_value:
            cursor = cursor.next
        return cursor

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode()
        last_unique_node = sentinel
        cursor = head
        while cursor:
            if cursor.next and cursor.val == cursor.next.val:
                cursor = self._skip_nodes_with_value(cursor.next, cursor.val)
                continue
            last_unique_node.next = cursor
            last_unique_node = last_unique_node.next
            cursor = cursor.next
        last_unique_node.next = None
        return sentinel.next