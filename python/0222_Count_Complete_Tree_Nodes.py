# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root):
        if(root==None):
            return 0

        return self.helper(root,self.mostLeftLevel(root,1),1)


    def helper(self,node,h,l):
        if(l==h):
            return 1
        if(self.mostLeftLevel(node.right,l+1)==h):
            return (1<<(h-l))+self.helper(node.right,h,l+1)
        else:
            return (1<<(h-l-1))+self.helper(node.left,h,l+1)

    def mostLeftLevel(self,root,level):
        while(root):
            level+=1
            root=root.left
        return level-1