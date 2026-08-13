# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast:
            if fast.next:
                fast = fast.next.next
                slow = slow.next
            else:
                break

        first = head
        second = slow.next
        curr = second
        slow.next = None
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        second = prev

        dummy = ListNode()
        tail = dummy

        currF = first
        currS = second
        count = 0

        while currF and currS:
            if (count % 2) == 0:
                tail.next = currF
                currF = currF.next

            else:
                tail.next = currS
                currS = currS.next
            
            tail = tail.next
            count += 1
        
        tail.next = currF or currS
        head = dummy.next

        return
