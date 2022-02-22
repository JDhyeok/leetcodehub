class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        
        ret = 0
        i = 0
        
        while i < len(columnTitle):
            ret = ret*26 + ord(columnTitle[i]) - ord('A') + 1
            i += 1
        
        return ret