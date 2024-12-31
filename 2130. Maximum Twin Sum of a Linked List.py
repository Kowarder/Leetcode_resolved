#In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.
#For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
#The twin sum is defined as the sum of a node and its twin.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        maxm = 0
        # find the mid
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        while slow:
            s_next = slow.next
            slow.next = prev
            prev = slow
            slow = s_next
        while prev:
            maxm = max(maxm, prev.val + head.val)
            prev = prev.next
            head = head.next
        return maxm
# in this problem, i first using slow and fast to make sure the mid of the linklist which is slow, and reserve the linklist from mid to the end
# finally, compare the max value of each element
