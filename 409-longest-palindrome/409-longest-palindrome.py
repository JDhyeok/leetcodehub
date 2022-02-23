class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        freq = {}
        ret = 0
        
        for letter in s:
            freq[letter] = freq.get(letter, 0) + 1
            
        exist_odd = False
        
        for key, val in freq.items():
            if val % 2 == 1:
                ret += val - 1
                exist_odd = True
            else:
                ret += val
        
        return ret + 1 if exist_odd == True else ret