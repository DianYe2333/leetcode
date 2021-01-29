# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root):
        if (root == None):
            return True
        q = list()
        flag = False

        q.append(root)
        while (len(q) > 0):
            Node = q.pop(0)
            if ((Node.left == None and Node.right) or (flag and Node.left)):
                return False
            if (Node.left):
                q.append(Node.left)
            if (Node.right):
                q.append(Node.right)
            else:
                flag = True

        return True