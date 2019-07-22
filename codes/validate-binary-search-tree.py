# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.prev = None
        self.flag = True
        def inorder(root):
            if root:
                inorder(root.left)
                if self.prev != None:
                    if self.prev.val >= root.val:
                        self.flag = False
                self.prev = root
                inorder(root.right)
        inorder(root)
        return self.flag
