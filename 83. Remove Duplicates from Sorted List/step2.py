# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cursor = head
        while cursor:
            seeking_next = cursor.next
            while seeking_next and seeking_next.val == cursor.val:
                seeking_next = seeking_next.next
            cursor.next = seeking_next
            cursor = cursor.next
        return head