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
        cursor = head
        while cursor:
            cursor.next = self._skip_nodes_with_value(cursor.next, cursor.val)
            cursor = cursor.next
        return head