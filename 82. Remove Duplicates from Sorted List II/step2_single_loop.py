# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode()
        last_unique_node = sentinel
        cursor = head
        remove_value = None
        while cursor:
            if cursor.val == remove_value:
                pass
            elif cursor.next and cursor.val == cursor.next.val:
                remove_value = cursor.val
            else:
                remove_value = None
                last_unique_node.next = cursor
                last_unique_node = last_unique_node.next
            cursor = cursor.next
        last_unique_node.next = None
        return sentinel.next
