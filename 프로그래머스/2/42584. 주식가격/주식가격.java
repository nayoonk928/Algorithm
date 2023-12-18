import java.util.*;

class Solution {
    public int[] solution(int[] prices) {
        int n = prices.length;
        int[] answer = new int[n];
        
        for (int i = 0; i < n - 1; i++) {
            int startPrice = prices[i];
            for (int j = i + 1; j < n; j++) {
                if (startPrice > prices[j]) {
                    answer[i] = j - i;
                    break;
                }
            }
            
            if (answer[i] == 0) {
                answer[i] = (n - 1) - i;
            }
        }
        
        return answer;
    }
}