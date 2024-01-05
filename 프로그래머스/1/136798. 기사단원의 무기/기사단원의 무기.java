import java.util.*;

class Solution {
    public int solution(int number, int limit, int power) {
        int answer = 0;
        int[] knight = new int[number + 1];
        
        for (int i = 1; i <= number; i++) {
            knight[i] = countDivisor(i);
        }
        
        for (int i = 1; i <= number; i++) {
            if (knight[i] > limit) {
                answer += power;
            } else {
                answer += knight[i];
            }
        }
        
        return answer;
    }
    
    private int countDivisor(int n) {
        int count = 0;
        for (int i = 1; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                if (i != Math.sqrt(n)) {
                    count += 2;
                } else {
                    count++;
                }
            }
        }
        
        return count;
    }
}