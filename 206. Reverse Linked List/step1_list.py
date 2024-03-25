# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        node_list = []
        cursor = head
        while cursor:
            node_list.append(cursor)
            cursor = cursor.next
        for i in range(len(node_list) - 1, 0, -1):
            node_list[i].next = node_list[i - 1]
        node_list[0].next = None
        return node_list[-1]