public class Solution {
    public String addBinary(String a, String b) {
        
        StringBuilder sb = new StringBuilder();
        
        int A = a.length() - 1, B = b.length() - 1, carry = 0;
        
        while(A >= 0 || B >= 0){
            int sum = carry;
            
            if(A >= 0)
                sum += a.charAt(A) - '0';
            if(B >= 0)
                sum += b.charAt(B) - '0';
            
            sb.append(sum % 2);
            carry = sum / 2;
            A--; B--;
        }
        
        if(carry > 0)
            sb.append(carry);
        
        return sb.reverse().toString();
    }
}