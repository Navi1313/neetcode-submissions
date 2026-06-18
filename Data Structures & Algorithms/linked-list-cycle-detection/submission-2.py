# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head :
            return False
        # curr = head
        # while curr.next is not None: 
        #     if curr.val > 1000:
        #         return True
        #     curr.val += 3000
        #     curr = curr.next
        # return False    
# Slow fast Pointer Approach 
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False     

