# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def _skip_nodes_with_value(self, head: Optional[ListNode], skip_value: int) -> Optional[ListNode]:
        while head and head.val == skip_value:
            head = head.next
        return head

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode()
        last_unique_node = sentinel
        cursor = head
        while cursor:
            if cursor.next and cursor.val == cursor.next.val:
                cursor = self._skip_nodes_with_value(cursor, cursor.val)
                continue
            last_unique_node.next = cursor
            last_unique_node = last_unique_node.next
            cursor = cursor.next
        last_unique_node.next = None
        return sentinel.next