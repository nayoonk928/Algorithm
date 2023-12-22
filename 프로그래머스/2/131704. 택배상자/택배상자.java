import java.util.*;

class Solution {
    public int solution(int[] order) {
        int answer = 0;
        Queue<Integer> main = new LinkedList<>();
        Stack<Integer> sub = new Stack<>();
        
        int firstBox = order[0];
        for (int i = firstBox; i <= order.length; i++) {
            main.add(i);
        }
        
        for (int i = 1; i < firstBox; i++) {
            sub.push(i);
        }
        
        for (int i = 0; i < order.length; i++) {
            int current = order[i];

            if (!main.isEmpty() && main.peek() == current) {
                main.poll();
                answer++;
            } else if (!sub.isEmpty() && sub.peek() == current) {
                sub.pop();
                answer++;
            } else {
                if (!main.isEmpty() && main.peek() < current) {
                    
                    while (current != main.peek()) {
                        sub.push(main.poll());
                    }
                    
                    answer++;
                    main.poll();
                } else {
                    break;
                }
            } 
        }
        
        return answer;
    }
}