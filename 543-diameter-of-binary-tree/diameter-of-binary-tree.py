# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # def depth(self, node):
    #     if not node:
    #         return 0
    #     left = self.depth(node.left)
    #     right = self.depth(node.right)

    #     return 1 + (left if left> right else right)
    
    # def diameterOfBinaryTree(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: int
    #     """
    #     return self.depth(root.left) + self.depth(root.right)
    def __init__(self):
        self.diameter = 0
    def depth(self, node):
        if not node:
            return 0
        left = self.depth(node.left)
        right = self.depth(node.right)
        if left + right > self.diameter:
            self.diameter = left + right

        return 1 + (left if left> right else right)
    
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.depth(root)
        return self.diameter