# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # curr = head
        # move = head
        # moveLen = 0
        # tailLen = 0

        
        # while move:
        #     moveLen += 1
        #     move = move.next

        #     if moveLen - tailLen > n:
        #        tailLen += 1
        #        curr = curr.next

        # curr.next = curr.next.next

        # return head

        fast = head
        remove = head

        for i in range(n):
            fast = fast.next

        if not fast:
            return head.next

        while fast.next:
            fast = fast.next
            remove = remove.next

        remove.next = remove.next.next

        return head
            

