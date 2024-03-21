# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        sorted_list_without_duplicate = ListNode(head.val)
        cursor = sorted_list_without_duplicate
        current_tail_value = cursor.val
        while head.next:
            head = head.next
            if head.val != current_tail_value:
                cursor.next = ListNode(head.val)
                cursor = cursor.next
                current_tail_value = head.val
        return sorted_list_without_duplicate

