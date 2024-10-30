# Given the head of a linked list, return the list after sorting it in ascending order.

# Input: head = [4,2,1,3]
# Output: [1,2,3,4]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lt = []
        temp = head
        while (temp != None):
            lt.append(temp.val)
            temp = temp.next
        
        lt.sort()
        temp = head
        for i in range(len(lt)):
            temp.val = lt[i]
            temp = temp.next
        return head

# in this problem, i use a very tricky method, first read the whole values to a list, and then sort the list in ascending order
# then insert to the list one by one
# i think it should has some normal methods to implement it
