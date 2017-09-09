class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        poisoned = False
        sum_time = 0
        finish_time = 0
        for timepoint in timeSeries:
            if not poisoned:
                poisoned = True
            else:
                if finish_time <= timepoint:
                    sum_time+=duration
                else:
                    sum_time+= timepoint - (finish_time - duration)
            finish_time = timepoint + duration
        if len(timeSeries)==0:
            return 0
        else:
            return sum_time + duration


if __name__ == '__main__':
    s = Solution()
    print(s.findPoisonedDuration([],11000))
