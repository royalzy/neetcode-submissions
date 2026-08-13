# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        currA = list1
        currB = list2
        dummy = ListNode()
        tail = dummy

        while currA and currB:
            if currA.val <= currB.val:
                tail.next = currA
                currA = currA.next
            else:
                tail.next = currB
                currB = currB.next
            
            tail = tail.next

        if currA:
            tail.next = currA

        if currB:
            tail.next = currB

        return dummy.next
            

                
                

        