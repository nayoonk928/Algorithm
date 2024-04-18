class Solution {
    public int solution(int n, int[] money) {
        int[] dp = new int[n + 1];
        dp[0] = 1; // 거스름돈이 0원일 때는 1가지 방법으로 거슬러 줄 수 있음
        
        // 동전 단위 별로 경우의 수 계산
        for (int coin : money) {
            for (int i = coin; i <= n; i++) {
                // 현재 동전을 사용하여 거스름돈을 i원을 거슬러주는 경우의 수는
                // 현재 동전을 사용하지 않았을 때의 경우의 수(dp[i])와
                // 현재 동전을 사용하여 거스름돈을 (i - coin)원을 거슬러주는 경우의 수(dp[i - coin])를 합친 것과 같음
                dp[i] = (dp[i] + dp[i - coin]) % 1000000007;
            }
        }
        
        return dp[n];
    }
}
