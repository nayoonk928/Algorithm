class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = arr.clone();
        
        for (int[] query : queries) {
            int index1 = query[0];
            int index2 = query[1];

            int temp = answer[index1];
            answer[index1] = answer[index2];
            answer[index2] = temp;
        }
        
        return answer;
    }
}