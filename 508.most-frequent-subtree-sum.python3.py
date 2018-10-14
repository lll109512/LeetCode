#
# [508] Most Frequent Subtree Sum
#
# https://leetcode.com/problems/most-frequent-subtree-sum/description/
#
# algorithms
# Medium (52.83%)
# Total Accepted:    38.3K
# Total Submissions: 72.6K
# Testcase Example:  '[5,2,-3]'
#
# 
# Given the root of a tree, you are asked to find the most frequent subtree
# sum. The subtree sum of a node is defined as the sum of all the node values
# formed by the subtree rooted at that node (including the node itself). So
# what is the most frequent subtree sum value? If there is a tie, return all
# the values with the highest frequency in any order.
# 
# 
# Examples 1
# Input:
# 
# ⁠ 5
# ⁠/  \
# 2   -3
# 
# return [2, -3, 4], since all the values happen only once, return all of them
# in any order.
# 
# 
# Examples 2
# Input:
# 
# ⁠ 5
# ⁠/  \
# 2   -5
# 
# return [2], since 2 happens twice, however -5 only occur once.
# 
# 
# Note:
# You may assume the sum of values in any subtree is in the range of 32-bit
# signed integer.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import Counter
class Solution:
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        self.dfs(root,res)
        c = Counter(res)
        m = max(c.values())
        return list(filter(lambda x: c[x] == m,c))

    def dfs(self,root,res):
        if not root:
            return 0
        S = root.val + self.dfs(root.left,res) + self.dfs(root.right,res)
        res.append(S)
        return S
        
        
