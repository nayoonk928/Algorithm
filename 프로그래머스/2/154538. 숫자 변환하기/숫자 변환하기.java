class Solution {
    public int solution(int x, int y, int n) {
        // 각 값을 x부터 y까지의 최소 단계로 도달하기 위한 배열 생성
        int[] dp = new int[y + 1];

        // x부터 y까지의 값을 반복 처리
        for (int i = x; i < y + 1; i++) {
        
            // 현재 값이 초기 값(x)과 같지 않고 이전에 도달한 적이 없으면 도달할 수 없는 값으로 표시(-1)
            if (i != x && dp[i] == 0) {
                dp[i] = -1;
                continue;
            }
            
            // 현재 값의 두 배를 계산하고 필요한 경우 최소 단계 업데이트
            if (i * 2 <= y) {
                dp[i * 2] = (dp[i * 2] == 0) ? dp[i] + 1 : Math.min(dp[i] + 1, dp[i * 2]);
            }
            
            // 현재 값의 세 배를 계산하고 필요한 경우 최소 단계 업데이트
            if (i * 3 <= y) {
                dp[i * 3] = (dp[i * 3] == 0) ? dp[i] + 1 : Math.min(dp[i] + 1, dp[i * 3]);
            }
            
            // 현재 값에 n을 더하고 필요한 경우 최소 단계 업데이트
            if (i + n <= y) {
                dp[i + n] = (dp[i + n] == 0) ? dp[i] + 1 : Math.min(dp[i] + 1, dp[i + n]);
            }
        }
        
        // 목표 값(y)에 도달하는 데 필요한 최소 단계 반환
        return dp[y];
    }
}