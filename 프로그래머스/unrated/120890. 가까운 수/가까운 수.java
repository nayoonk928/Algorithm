class Solution {
    public int solution(int[] array, int n) {
        int answer = Integer.MAX_VALUE;
        int min = Integer.MAX_VALUE;
        
        for (int i = 0; i < array.length; i++) {
            int sub = Math.abs(n - array[i]);
            if (min > sub) {
                min = sub;
                answer = array[i];
            } else if (min == sub) {
                answer = Math.min(answer, array[i]);
            }
        }
        
        return answer;
    }
}