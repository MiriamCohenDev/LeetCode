# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        result = []
        self.retInorder(root, result)
        return result
        
    
    def retInorder(self, root, result):
        if root == None:
            return
        self.retInorder(root.left, result)
        result.append(root.val)
        self.retInorder(root.right, result)

        