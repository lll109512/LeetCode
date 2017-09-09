# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return []
        max_depth=self.depth(root)
        Li=[[] for _ in range(max_depth)]
        Li=self.sy(root,0,Li)
        #print(Li)
        for i in range(len(Li)):
            if i%2==1:
                Li[i]==Li[i].reverse()
        return Li


    def depth(self,root):
        if not root:
            return 0
        return max(self.depth(root.left), self.depth(root.right))+1

    def sy(self,root,depth,List):
        if root:
            List[depth].append(root.val)
        else:
            return
        self.sy(root.left,depth+1,List)
        self.sy(root.right,depth+1,List)
        return List


if __name__ == '__main__':
    s=Solution()
    root=TreeNode(0)
    root.left=TreeNode(1)
    root.right=TreeNode(1)
    print(s.isSymmetric(root))
