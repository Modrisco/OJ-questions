"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        travesal = []
        if not root:
            return []
        if root.val is not None:
            travesal.append(root.val)
        if root.children:
            roots = root.children
        else:
            return travesal
        roots = roots[::-1]
        while roots != []:
            r = roots.pop()
            travesal.append(r.val)
            if r.children:
                roots += r.children[::-1]
        return travesal
