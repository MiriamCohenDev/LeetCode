# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        res = ListNode()
        f = res
        mod = 0
        while l1!= None or l2!=None or mod != 0:
            f.next = ListNode()
            f = f.next
            if l1 !=None:
                mod+=l1.val
                l1 = l1.next
            if l2 != None:
                mod += l2.val
                l2 = l2.next
            f.val = mod%10
           
            mod = mod//10

        return res.next
        
            

        