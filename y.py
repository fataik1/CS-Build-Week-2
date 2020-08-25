#ADDing 2 numbers w 2 non empty linked-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #put a node so you do not deal with edge cases in LL
        fake = ListNode()
        # cur is the point at position we will be putting the new node/digit 
        cur = fake
        
        #out of loop. set to 0
        carry = 0
        #want to iterate through the nodes while either has a digit
        while l1 or l2 or carry:
            #v1 is digit of list1.. if l1 is non-null  set to 0 
            v1 = l1.val if l1 else 0
            #same thing for l2
            v2 = l2.val if l2 else 0
            

        