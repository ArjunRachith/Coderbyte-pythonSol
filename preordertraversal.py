# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if root == None:
            return res
            
        cur_level = [root]
        while cur_level != []:
            n = cur_level[0]
            res.append(n.val)
            cur_level = cur_level[1:]
            if n.right != None:
                cur_level = [n.right] + cur_level
            if n.left != None:
                cur_level = [n.left] + cur_level   
            
        return res
                
