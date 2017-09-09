# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and q:
            return self.same(p,q)
        elif p==None and q==None:
            return True
        else:
            return False


    def same(self,p_root,q_root):
        p_node,q_node=p_root.left,q_root.left
        result=True
        if (q_node==None or p_node==None) and q_node!=p_node:
            return False
        if p_node and q_node:
            result=result and self.same(p_node,q_node)
        p_node,q_node=p_root.right,q_root.right
        if (q_node==None or p_node==None) and q_node!=p_node:
            return False
        if p_node and q_node:
            result=result and self.same(p_node,q_node)
        if p_root.val!=q_root.val:
            return False
        return True and result
