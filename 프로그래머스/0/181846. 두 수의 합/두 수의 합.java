import java.math.*;

public class Solution {
    public String solution(String a, String b) {
        BigInteger num1 = new BigInteger(a);
        BigInteger num2 = new BigInteger(b);
        BigInteger sum = num1.add(num2);
        
        return String.valueOf(sum);
    }
}
