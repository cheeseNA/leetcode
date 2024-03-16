# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_dummy_head = ListNode()
        sum_cursor = sum_dummy_head
        carry = 0
        while l1 is not None or l2 is not None or carry > 0:
            l1_digit = l1.val if l1 else 0
            l2_digit = l2.val if l2 else 0
            digit_sum = l1_digit + l2_digit + carry
            carry = digit_sum // 10
            digit_val = digit_sum % 10
            
            sum_cursor.next = ListNode(digit_val)
            sum_cursor = sum_cursor.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return sum_dummy_head.next


