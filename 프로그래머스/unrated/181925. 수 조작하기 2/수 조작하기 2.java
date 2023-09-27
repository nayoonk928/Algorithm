class Solution {
    public String solution(int[] numLog) {
        StringBuilder answer = new StringBuilder();
        
        for (int i = 1; i < numLog.length; i++) {
            int prev = numLog[i - 1];
            int current = numLog[i];
            
            if (current - prev == 1) {
                answer.append('w');
            } else if (current - prev == -1) {
                answer.append('s');
            } else if (current - prev == 10) {
                answer.append('d');
            } else if (current - prev == -10) {
                answer.append('a');
            }
        }
        
        return answer.toString();
    }
}