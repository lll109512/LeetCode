# class TreeNode(object):
def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        global node_list
        node_list = []
        self.mind(root)
        node_list.sort()
        new_list = []
        for i in range(len(node_list)):
            if i + 1<len(node_list):
                new_list.append(node_list[i+1]-node_list[i])

        return min(new_list)

    def mind(self,root):
        if not root:
            return None
        node_list.append(root.val)
        self.mind(root.left)
        self.mind(root.right)
