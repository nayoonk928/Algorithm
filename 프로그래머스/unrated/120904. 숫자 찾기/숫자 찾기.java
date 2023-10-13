class Solution {
    public int solution(int num, int k) {
        String numStr = Integer.toString(num);
        
        for (int i = 0; i < numStr.length(); i++) {
            if (numStr.charAt(i) - '0' == k) {
                return i + 1;
            }
        }
        
        return -1;
    }
}