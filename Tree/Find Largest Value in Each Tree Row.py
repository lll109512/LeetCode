from Queue import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        qu = deque()
        qu.append([root])
        result = []
        while qu:
            root_list = qu.popleft()
            result.append(max(root_list,key=lambda x:x.val).val)
            next_layer = []
            for ro in root_list:
                if ro.left:
                    next_layer.append(ro.left)
                if ro.right:
                    next_layer.append(ro.right)
            if next_layer:
                qu.append(next_layer)
        return result
