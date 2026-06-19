"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def find(cur1 , cur2 , x):
            if x is None:
                return None

            while cur1 != x:
                cur1 = cur1.next
                cur2 = cur2.next
            return cur2    


        dummy = Node(0)
        curr = head
        copy_curr = dummy
        while curr:
            new_node = Node(curr.val)
            copy_curr.next = new_node
            copy_curr = copy_curr.next
            curr = curr.next
        head2 = dummy.next

        curr1 = head
        curr2 = head2

        while curr1:
            curr2.random = find(head , head2 , curr1.random)
            curr2 = curr2.next
            curr1 = curr1.next

        return head2



