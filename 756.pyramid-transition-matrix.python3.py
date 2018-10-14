#
# [757] Pyramid Transition Matrix
#
# https://leetcode.com/problems/pyramid-transition-matrix/description/
#
# algorithms
# Medium (47.67%)
# Total Accepted:    7.8K
# Total Submissions: 16.3K
# Testcase Example:  '"ABC"\n["ABD","BCE","DEF","FFF"]'
#
#
# We are stacking blocks to form a pyramid.  Each block has a color which is a
# one letter string, like `'Z'`.
#
# For every block of color `C` we place not in the bottom row, we are placing
# it on top of a left block of color `A` and right block of color `B`.  We are
# allowed to place the block there only if `(A, B, C)` is an allowed triple.
#
# We start with a bottom row of bottom, represented as a single string.  We
# also start with a list of allowed triples allowed.  Each allowed triple is
# represented as a string of length 3.
#
# Return true if we can build the pyramid all the way to the top, otherwise
# false.
#
#
# Example 1:
#
# Input: bottom = "XYZ", allowed = ["XYD", "YZE", "DEA", "FFF"]
# Output: true
# Explanation:
# We can stack the pyramid like this:
# ⁠   A
# ⁠  / \
# ⁠ D   E
# ⁠/ \ / \
# X   Y   Z
#
# This works because ('X', 'Y', 'D'), ('Y', 'Z', 'E'), and ('D', 'E', 'A') are
# allowed triples.
#
#
#
# Example 2:
#
# Input: bottom = "XXYX", allowed = ["XXX", "XXY", "XYX", "XYY", "YXZ"]
# Output: false
# Explanation:
# We can't stack the pyramid to the top.
# Note that there could be allowed triples (A, B, C) and (A, B, D) with C !=
# D.
#
#
#
# Note:
#
# bottom will be a string with length in range [2, 8].
# allowed will have length in range [0, 200].
# Letters in all strings will be chosen from the set {'A', 'B', 'C', 'D', 'E',
# 'F', 'G'}.
#
#
#

from itertools import product


class Solution:
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        if not bottom:
            return True
        if not allowed:
            return False
        return self.dfs(bottom, allowed)

    def dfs(self, bottom, allowed):
        if len(bottom) == 1:
            return True

        possibles = []
        i = 0
        while i < len(bottom) - 1:
            top = [z[2] for z in allowed
                   if z[0] == bottom[i] and z[1] == bottom[i+1]]
            if not top:
                return False
            possibles.append(top)
            i += 1
        for top in product(*possibles):
            if self.dfs(top, allowed):
                return True

        return False
