# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        if head == None:
            return head
        if head.next == None:
            return head
        help1 = head
        help2 = head.next
        help1.next = help2.next
        help2.next = help1
        head = help2
        head2 = help1
        help1 = help1.next
        while help1 != None and help1.next != None:
            help2 = help1.next
            help1.next = help2.next
            help2.next = help1
            head2.next = help2
            head2 = help1
            help1 = help1.next
            
            
        return head

        