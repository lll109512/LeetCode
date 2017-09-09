import heapq
from collections import Counter
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        lt = list(s)
        counter = Counter(lt)
        d = {}
        new_list = []
        for key,value in counter.items():
            d[key*value] = value
        for i in set(lt):
            new_list.append(counter[i]*i)
        ans = heapq.nlargest(len(new_list),new_list,key = lambda x: d[x])
        return ''.join(ans)


if __name__ == '__main__':
    s = Solution()
    s.frequencySort('loveleetcode')
