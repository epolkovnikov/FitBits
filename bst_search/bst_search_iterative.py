import unittest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def __init__(self):
        self.rv = []
        
    def print_subtree(self, root):
        if root is not None:
            self.rv.append(root.val)
            print(f"sub: {root.val}")
            self.print_subtree(root.left)
            self.print_subtree(root.right)
        return self.rv

    
    def searchBST(self, root, val):
        while root is not None:
            if root.val == val:
                break
            else:
                if val < root.val:
                    root = root.left
                else:
                    root = root.right
        return root
                       

exec(open("./test.py").read())
