import java.util.*;

class Solution {
    public int[] solution(int k, int[] score) {
        int days = score.length;
        int[] answer = new int[days];
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        
        for (int i = 0; i < days; i++) {
            if (pq.size() < k) {
                pq.add(score[i]);
                answer[i] = pq.peek();
            } else {
                if (pq.peek() > score[i]) {
                    answer[i] = pq.peek();
                    continue;
                }
                
                pq.remove();
                pq.add(score[i]);
                answer[i] = pq.peek();
            }
        }
        
        return answer;
    }
}