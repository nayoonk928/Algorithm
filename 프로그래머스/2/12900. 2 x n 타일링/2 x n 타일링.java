import java.util.*;

class Solution {
    public int solution(int n) {
        int[] dp = new int[n + 1];
        Arrays.fill(dp, -1);
        return countCombinations(n, dp);
    }
    
    private int countCombinations(int remaining, int[] dp) {
        if (remaining < 0) {
            return 0;
        }
        
        if (remaining == 0) {
            return 1;
        }
        
        // 이미 계산된 값이 있는 경우
        if (dp[remaining] != -1) {
            return dp[remaining];
        }
        
        // 계산된 값이 없는 경우 재귀 -> 1을 사용한 경우 + 2를 사용한 경우
        dp[remaining] = countCombinations(remaining -1, dp) + countCombinations(remaining -2, dp);
        dp[remaining] %= 1000000007;
        return dp[remaining];
    }
}