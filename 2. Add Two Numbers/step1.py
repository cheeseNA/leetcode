# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_root_node = ListNode()
        sum_cursor = sum_root_node
        carry = 0
        while True:
            digit_sum = None
            if l1 is None and l2 is None:
                if carry != 0:
                    sum_cursor.next = ListNode(val=carry)
                break
            if l1 is not None and l2 is None:
                digit_sum = carry + l1.val
                l1 = l1.next
            elif l1 is None and l2 is not None:
                digit_sum = carry + l2.val
                l2 = l2.next
            else:
                digit_sum = carry + l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            carry = digit_sum // 10
            digit_value = digit_sum % 10
            sum_cursor.next = ListNode(val=digit_value)
            sum_cursor = sum_cursor.next
        return sum_root_node.next

