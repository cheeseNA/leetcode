# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(val=0, next=head)
        current_tail = dummy_head
        cursor = head
        while cursor:
            if (not cursor.next) or cursor.val != cursor.next.val:
                current_tail.next = cursor
                current_tail = current_tail.next
                cursor = cursor.next
            else:
                while cursor.next and cursor.val == cursor.next.val:
                    cursor = cursor.next
                cursor = cursor.next
                if not cursor:
                    current_tail.next = None
                    break
        return dummy_head.next