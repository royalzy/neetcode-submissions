# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        thought process
        two pointers
        for each curr in l1 and l2
        add the nums
        val = sum % 10 
        if theres a carry over bring over to next node
        '''

        carry_over = 0
        cur1 = l1
        cur2 = l2
        dummy = ListNode()
        res = dummy

        while cur1 or cur2 or carry_over:
            val1 = cur1.val if cur1 else 0
            val2 = cur2.val if cur2 else 0
            total = val1 + val2 + carry_over

            carry_over = total // 10
            val_to_store = total % 10
            res.next = ListNode(val_to_store)
            res = res.next
            if cur1: cur1 = cur1.next
            if cur2: cur2 = cur2.next


        res.next = cur1 or cur2

        return dummy.next