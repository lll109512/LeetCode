import heapq
from collections import Counter
#heap
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dty=dict()
        for x in nums:
            if x in dty:
                dty[x]+=1
            else:
                dty[x]=1
        List=list(zip(dty.keys(),dty.values()))
        heapq.heapify(List)
        result=heapq.nlargest(k,List,key=lambda List:List[1])
        return list(list(zip(*result))[0])


#more faster way
#so esay QAQ
    def topKFrequent2(self, nums, k):
        #return [ c for c, _ in Counter(nums).most_common(k) ]
        return list(list(zip(*Counter(nums).most_common(k)))[0])

if __name__ == '__main__':
    x=Solution()
    print(x.topKFrequent([1,1,2,2,2,3],3))
