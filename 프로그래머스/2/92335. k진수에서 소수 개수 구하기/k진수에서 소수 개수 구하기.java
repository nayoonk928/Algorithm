import java.util.*;

class Solution {
    public int solution(int n, int k) {
        int answer = 0;
        
        String s = Integer.toString(n, k);
        String[] array = s.split("0");
        
        for (String a : array) {
            if (!a.isEmpty() && isPrime(Long.parseLong(a))) {
                answer++;
            }
        }
        
        return answer;
    }
    
    private boolean isPrime(long num) {
        if (num < 2) {
            return false;
        }
        
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) {
                return false;
            }
        }
        
        return true;
    }
}