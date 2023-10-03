class Solution {
    public String solution(int q, int r, String code) {
        StringBuilder answer = new StringBuilder();
        char[] chars = code.toCharArray();
        
        for (int i = 0; i < chars.length; i++) {
            if (i % q == r) {
                answer.append(chars[i]);
            }
        }
        
        return answer.toString();
    }
}