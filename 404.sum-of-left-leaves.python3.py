#
# [404] Sum of Left Leaves
#
# https://leetcode.com/problems/sum-of-left-leaves/description/
#
# algorithms
# Easy (48.02%)
# Total Accepted:    101.9K
# Total Submissions: 212.2K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Find the sum of all left leaves in a given binary tree.
# 
# Example:
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# There are two left leaves in the binary tree, with values 9 and 15
# respectively. Return 24.
# 
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        b = []
        a = self.isleaf(root, b)
        print(a)
        sum = 0
        for i in range(0, len(a), 1):
            sum = sum + a[i]

        return sum

    def isleaf(self, root, a):
        if not root:
            return a
        elif root.left and (not root.left.left and not root.left.right):
             a.append(root.left.val)

        self.isleaf(root.left, a)
        self.isleaf(root.right, a)
        return a
