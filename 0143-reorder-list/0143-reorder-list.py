# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        while head and head.next and head.next.next:
            tail = head

            while tail.next:
                prev = tail
                tail = tail.next
            
            prev.next = None
            
            temp = head.next
            head.next = tail
            head = head.next

            head.next = temp
            head = head.next