# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # O(N) + O(N) sPACE 
        arr = []
        curr = head
        while curr :
            arr.append(curr.val)
            curr = curr.next
        # Now make the k = k%n becoz k value may be greater then n 
        curr = head
        n = len(arr)
        k %= n
        # last k elemts in array will be copied to top nodes in Linked List
        # copy element from k postions
        for i in range(n-k , n):
            curr.val = arr[i]
            curr = curr.next
        # in LL cpoy the elements of whole node 
        # Ex -> k = 3 -> top k elemets will get into remaining nodes 
        for i in range(n-k):
            curr.val = arr[i]
            curr = curr.next

        return head    

