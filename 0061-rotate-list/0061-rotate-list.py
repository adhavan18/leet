# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #nothing changes, returns the same. head.
        if not head or not head.next or k == 0:
            return head
        #find the length of the list
        n = 1
        tail = head
        while tail.next:
            tail = tail.next
            n += 1
        tail.next = head
        k = k % n
        if k == 0:
            tail.next = None
            return head
        #tail is at position (n - k - 1) from the start
        steps_to_new_tail = n - k - 1
        new_tail = head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next
        #node after new_tail becomes the new head
        new_head = new_tail.next
        #break the circular link to finalize the list
        new_tail.next = None
        return new_head