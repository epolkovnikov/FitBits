# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:

    def __init__(self):
        self.rv = []
        self.rt = None

    def print_subtree(self, root):
        if root is not None:
            self.rv.append(root.val)
            print(f"sub: {root.val}")
            self.print_subtree(root.left)
            self.print_subtree(root.right)
        return self.rv

    def searchRec(self, root, val):
        if root is not None:
            if root.val == val:
                self.rt = root
                # we are not calling anything, so the recursion should end here
                # we store the result to the property,
                # because return does not work in recursion stack
            else:
                if val < root.val:
                    self.searchRec(root.left, val)
                else:
                    self.searchRec(root.right, val)
        
    def searchBST(self, root, val):
        self.searchRec(root, val)
        return self.rt
                       

exec(open("./test.py").read())
