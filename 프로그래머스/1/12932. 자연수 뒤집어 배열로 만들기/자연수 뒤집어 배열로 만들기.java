class Solution {
    public int[] solution(long n) {
        
        StringBuilder sb = new StringBuilder(Long.toString(n));
        sb.reverse();
        
        int len = sb.length();
        int[] answer = new int[len];
        
        for (int i = 0; i < len; i++) {
            answer[i] = Integer.parseInt(sb.substring(i, i + 1));
        }
        
        return answer;
    }
}