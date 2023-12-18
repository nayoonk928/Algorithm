import java.util.*;

class Solution {
    public int solution(int[] topping) {
        int answer = 0;
        int n = topping.length;

        Set<Integer> first = new HashSet<>();
        Map<Integer, Integer> second = new HashMap<>();
        
        for (int i = 0; i < n; i++) {
            second.put(topping[i], second.getOrDefault(topping[i], 0) + 1);
        }
        
        for (int i = 0; i < n - 1; i++) {
            first.add(topping[i]);
            second.put(topping[i], second.get(topping[i]) - 1);
            
            if (second.get(topping[i]) == 0) {
                second.remove(topping[i]);
            }
            
            if (first.size() == second.size()) answer++;
        }

        return answer;
    }
}