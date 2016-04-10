"""
[ref.href] leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree
"
  Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
"
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
    
        stack = []
    
        ptrace = set()
        
        node = root
        while node != None:
            ptrace.add(node)
            if node.val > p.val:
                node = node.left
            elif node.val < p.val:
                node = node.right
            else:
                break
        
        qtrace = set()
        
        node = root
        while node != None:
            if node in ptrace:
                stack.append(node)
            qtrace.add(node)
            if node.val > q.val:
                node = node.left
            elif node.val < q.val:
                node = node.right
            else:
                break
        
        if len(stack) < 1:
            raise ValueError("p and q are not on the same tree")
        return stack.pop()
