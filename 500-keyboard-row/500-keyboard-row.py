class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
        ret = []
        
        high = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i','o', 'p']
        mid = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k' , 'l']
        low = ['z', 'x', 'c', 'v', 'b', 'n', 'm']
        
        for word in words:
            lword = word.lower()
            
            row = 0
            
            if all(True if c in high else False for c in lword):
                ret.append(word)
            elif all(True if c in mid else False for c in lword):
                ret.append(word)
            elif all(True if c in low else False for c in lword):
                ret.append(word)
            
        return ret
        
        