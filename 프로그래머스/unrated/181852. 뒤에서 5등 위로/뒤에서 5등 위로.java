import java.util.*;

class Solution {
    public int[] solution(int[] num_list) {
        List<Integer> answer = new ArrayList<>();
        
        Arrays.sort(num_list);
        
        for (int i = 5; i < num_list.length; i++) {
            answer.add(num_list[i]);
        }
        
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}