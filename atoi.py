import re
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        re.findall('[0-9]', string, flags=0)
        str = re.findall('(^[\+\-0]*\d+)\D*', str)
        print(str)
        try:
            result = int(''.join(str))
            if result > 2147483647:
                return 2147483647
            elif result < -2147483648:
                return -2147483648
            else:
                return result
        except Exception as e:
            return 0



if __name__ == '__main__':
    s = Solution()
    s.myAtoi('')
