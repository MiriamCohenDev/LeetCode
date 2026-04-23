# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        return self.retMiddle(nums, 0, len(nums))
        
    def retMiddle(self, nums, first, last):
        if first >= last:
            return None
        middle = (first + last)//2
        return TreeNode(nums[middle], self.retMiddle(nums, first, middle), self.retMiddle(nums, middle+1, last))
