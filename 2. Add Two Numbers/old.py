# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def listNodeToNumber(self, l: ListNode) -> int:
        node = l
        power = 1
        number = 0
        
        while node is not None:
            number += power * node.val
            power *= 10
            node = node.next
        
        return number
    
    def numberToListNode(self, number: int) -> ListNode:
        start = ListNode(val=number % 10)
        now = start
        number //= 10
        while number > 0:
            now.next = ListNode(val=number % 10)
            now = now.next
            number //= 10
        return start

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1num = self.listNodeToNumber(l1)
        l2num = self.listNodeToNumber(l2)
        return self.numberToListNode(l1num + l2num)

        