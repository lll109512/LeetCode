# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        Node=None
        if not preorder:
            return []
        return self.build(preorder,inorder,None)


#my
    def build(self,preorder,inorder,root):
        if len(inorder)==1:
            if root==None:
                root=TreeNode(preorder[0])
            return root
        root_val=preorder[0]
        next_node_val=preorder[1]
        #root=TreeNode(root_val)
        if root==None:
            root=TreeNode(root_val)
        if inorder.index(next_node_val) < inorder.index(root_val):
            root.left=TreeNode(next_node_val)
            self.build(preorder[1:],inorder[:inorder.index(root_val)],root.left)
            for i in range(len(preorder)):
                if preorder[i] in inorder and inorder.index(preorder[i]) > inorder.index(root_val):
                    root.right=TreeNode(preorder[i])
                    self.build(preorder[i:],inorder[inorder.index(root_val)+1:],root.right)
                    break
        else:
            root.right=TreeNode(next_node_val)
            self.build(preorder[1:],inorder[inorder.index(root_val)+1:],root.right)
        return root

#others
    def buildTree(self,preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return None
        prev = None
        root = TreeNode(preorder[0])
        stack = [root]
        poi = 1 #preorder index
        ioi = 0 #inorder index
        while poi < len(preorder):
            if len(stack) > 0 and stack[-1].val == inorder[ioi]:
                ioi += 1
                prev = stack[-1]  #top of stack
                stack.pop()
            else:
                nn = TreeNode(preorder[poi])
                if prev == None:
                    stack[-1].left = nn
                elif prev != None:
                    prev.right = nn
                    prev = None
                stack.append(nn)
                poi += 1


#easy to understand
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        self.preindex = 0
        ind = {v:i for i, v in enumerate(inorder)}
        head = self.dc(0, len(preorder) - 1, preorder, inorder, ind)
        return head

    def dc(self, start, end, preorder, inorder, ind):
        if start <= end:
            mid = ind[preorder[self.preindex]]
            self.preindex += 1
            root = TreeNode(inorder[mid])
            root.left = self.dc(start, mid - 1, preorder, inorder, ind)
            root.right = self.dc(mid + 1, end, preorder, inorder, ind)
            return root
