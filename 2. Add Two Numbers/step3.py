# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def add_two_numbers_helper(l1: Optional[ListNode], l2: Optional[ListNode], carry: int) -> Optional[ListNode]:
            if l1 is None and l2 is None and carry == 0:
                return None
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            digit_sum = l1_val + l2_val + carry

            sum_root_node = ListNode(val=digit_sum%10)
            l1_next = l1.next if l1 else None
            l2_next = l2.next if l2 else None
            sum_root_node.next = add_two_numbers_helper(l1_next, l2_next, digit_sum // 10)
            return sum_root_node
        return add_two_numbers_helper(l1, l2, 0)