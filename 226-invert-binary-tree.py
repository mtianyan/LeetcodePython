# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root

class Solution:
    """
    非递归实现
    """
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        tempqueue = [root]
        while tempqueue:
            node = tempqueue.pop()
            tempnode = node.left
            node.left = node.right
            node.right = tempnode
            if node.left:
                tempqueue.append(node.left)
            if node.right:
                tempqueue.append(node.right)
        return root