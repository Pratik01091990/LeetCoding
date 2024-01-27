# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        pointer = head
        while head.next is not None:
            if head.val == head.next.val:
                #deleteNode()
                head.next = head.next.next
            else:
                head = head.next
        
        return pointer