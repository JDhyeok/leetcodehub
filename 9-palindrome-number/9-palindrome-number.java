class Solution {
    public boolean isPalindrome(int x) {
        if(x < 0)
            return false;
        
        int originX = x;
        int reverseX = 0;
        
        while(x > 0){
            reverseX = reverseX*10 + (x % 10);
            x /= 10;
        }
        
        return (originX == reverseX);
    }
}