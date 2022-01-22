class Solution:
    def makeDictionary(self, word):
        letters = {}
        
        for ch in word:
            ch = ch.lower()
            
            if not 'a' <= ch and ch <= 'z':
                continue
            if letters.get(ch) == None:
                letters[ch] = 1
            else:
                letters[ch] += 1
                
        return letters
    
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        
        letters = self.makeDictionary(licensePlate)
        min_length = 987654321
        ans  = ""
        
        for word in words:
            tmp = self.makeDictionary(word)
            
            complete = True
            for key, val in letters.items():
                if tmp.get(key) == None or tmp.get(key) < val:
                    complete = False
                    break
            
            if complete == True and len(word) < min_length:
                ans = word
                min_length = len(word)
        
        return ans