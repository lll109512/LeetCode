#
# [56] Merge Intervals
#
# https://leetcode.com/problems/merge-intervals/description/
#
# algorithms
# Medium (33.15%)
# Total Accepted:    249.1K
# Total Submissions: 748.4K
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# Given a collection of intervals, merge all overlapping intervals.
# 
# Example 1:
# 
# 
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into
# [1,6].
# 
# 
# Example 2:
# 
# 
# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considerred overlapping.
# 
#
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        sortedIntervals = sorted(intervals,key=lambda x:x.start)
        me = max(sortedIntervals,key=lambda x:x.end).end
        sortedIntervals += [Interval(me+1,me+1)]
        result = []
        for i in range(1,len(sortedIntervals)):
            if sortedIntervals[i-1].end >= sortedIntervals[i].start:
                sortedIntervals[i].start = sortedIntervals[i-1].start
                if sortedIntervals[i-1].end >= sortedIntervals[i].end:
                    sortedIntervals[i].end = sortedIntervals[i-1].end
            else:
                result.append(sortedIntervals[i-1])
        
        return result
        
