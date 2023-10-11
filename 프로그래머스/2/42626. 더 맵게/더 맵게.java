import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        
        for (int s : scoville) {
            pq.offer(s);
        }
        
        while(pq.peek() < K) {
            int first = pq.poll();
            int second = pq.poll();
            int mix = first + (second * 2);
            pq.offer(mix);
            answer++;
            
            if (pq.size() == 1 && pq.peek() < K) {
                return -1;
            }
        }
        
        return answer;
    }
}