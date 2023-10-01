class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        
        for (int num : num_list) {
            int temp = num;
            while (temp != 1) {
                if (temp % 2 == 0) {
                    temp /= 2;
                    answer++;
                } else {
                    temp--;
                    temp /= 2;
                    answer++;
                }
            }        
        }
        
        return answer;
    }
}