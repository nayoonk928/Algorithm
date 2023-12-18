import java.util.*;

class Solution {
    int solution(int[][] land) {
        int[][] dp = new int[land.length][land[0].length];

        for (int i = 0; i < land.length; i++) {
            dp[i] = Arrays.copyOf(land[i], land[i].length);
        }
        
        int answer = Integer.MIN_VALUE;
        for (int i = 1; i < land.length; i++) {
            for (int j = 0; j < 4; j++) {
                int max = Integer.MIN_VALUE;
                
                for (int k = 0; k < 4; k++) {
                    if (k != j) {
                        max = Math.max(max, dp[i - 1][k]);
                    }
                }

                dp[i][j] += max;
                answer = Math.max(answer, dp[i][j]);
            }
        }
        
        return answer;
    }
}