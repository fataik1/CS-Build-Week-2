# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # if not the list1 return list2 and vice versa
        if not l1:
            return l2
        if not l2:
            return l1
        # set this to None
        this = None
        # if the value of list 1 is less than l2 value
        if l1.val < l2.val:
            # create variable this = to l1
            this = l1
            #check the next node and = l1 next iteration and l2
            this.next = self.mergeTwoLists(l1.next, l2)
        else:
            #create variable this = to l2
            this = l2
            #check the next node an d= l2 next iteration and l1
            this.next = self.mergeTwoLists(l1, l2.next)
            
        return this
                
        