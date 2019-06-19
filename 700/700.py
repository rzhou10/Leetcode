'''
    Search in a Binary Search Tree
    Runtime: 84 ms
'''

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        
        if not root or root.val == val:
            return root
        
        elif val < root.val:
            return self.searchBST(root.left, val)
        
        else:
            return self.searchBST(root.right, val)