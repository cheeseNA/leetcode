# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        head_of_list_without_duplicate = head
        current_tail = head
        while head.next:
            head = head.next
            if head.val != current_tail.val:
                current_tail.next = head
                current_tail = head
        current_tail.next = None
        return head_of_list_without_duplicate