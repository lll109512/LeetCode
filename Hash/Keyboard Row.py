class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        first_row = 'qwertyuiop'
        second_row = 'asdfghjkl'
        third_row = 'zxcvbnm'
        Table = {}
        result = []
        for i in first_row:
            Table[i] = 1
        for i in second_row:
            Table[i] = 2
        for i in third_row:
            Table[i] = 3
        for word in words:
            clss = Table[word[0].lower()]
            lable = True
            for x in word:
                if clss != Table[x.lower()]:
                    lable = False
                    break
            if lable:
                result.append(word)
        return result


if __name__ == '__main__':
    s = Solution()
    for x in s.findWords(["Hello","Alaska","Dad","Peace"]):
        print(x)
