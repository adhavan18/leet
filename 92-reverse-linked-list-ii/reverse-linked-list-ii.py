# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        #reverse list
        #node = None
        #temp = head.next
        #head.next = node 
        #node = head
        #head = temp
        #return node
        if left == right:
            return head
        dummy = ListNode(0)
        dummy.next = head

        left_prev = dummy
        curr = head

        for _ in range(left - 1):
            left_prev = curr
            curr = curr.next

        sublist_tail = curr
        prev = None
        
        for _ in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        left_prev.next = prev
        sublist_tail.next = curr

        return dummy.next        