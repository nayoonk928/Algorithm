class Solution {
    public int[] solution(String myString) {
        String[] str = myString.split("x", -1);
        
        int n = str.length;
        int[] answer = new int[n];
        
        for (int i = 0; i < n; i++) {
            answer[i] = str[i].length();
        }
        
        return answer;
    }
}