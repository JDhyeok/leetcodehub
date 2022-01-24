class Solution:
    def detectCapitalUse(self, word: str) -> bool:        

        # all capital or not all
        if word.isupper() == True or word.islower() == True:
            return True
        
        # Only first letter capital
        if word.title() == word:
            return True
            
        return False