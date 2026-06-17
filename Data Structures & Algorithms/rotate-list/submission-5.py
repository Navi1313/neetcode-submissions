# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # O(N) + O(N) sPACE 
        # if not head:
        #     return None
        # arr = []
        # curr = head
        # while curr :
        #     arr.append(curr.val)
        #     curr = curr.next
        # # Now make the k = k%n becoz k value may be greater then n 
        # curr = head
        # n = len(arr)
        # k %= n
        # # last k elemts in array will be copied to top nodes in Linked List
        # # copy element from k postions
        # for i in range(n-k , n):
        #     curr.val = arr[i]
        #     curr = curr.next
        # # in LL cpoy the elements of whole node 
        # # Ex -> k = 3 -> top k elemets will get into remaining nodes 
        # for i in range(n-k):
        #     curr.val = arr[i]
        #     curr = curr.next
        # return head

# -------------------------------------------------------------------------------------
        # O(n) Time and O(1) Space 

        # count the total no of Nodes

        # if not head or not head.next or k==0:
        #     return head
    
        # tail = head
        # count = 1 
        # while tail.next:
        #     tail = tail.next
        #     count +=1
        
        # k = k%count  
        # if k == 0 :
        #     return head
            
        # curr = head
        # for i in range(count-k-1):
        #     curr = curr.next

        # new_head = curr.next
        # curr.next = None
        # tail.next = head

        # return new_head    

    # circular loop then disconnect 
        if not head or not head.next or k==0 :
            return head
        tail = head
        count = 1 
        while tail.next:
            tail = tail.next
            count +=1
        tail.next = head
        k = k%count

        for i in range(count-k):
            tail = tail.next
        head = tail.next
        tail.next = None
        return head    








        



