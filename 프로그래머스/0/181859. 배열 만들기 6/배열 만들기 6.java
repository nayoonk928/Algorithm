import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        List<Integer> answer = new ArrayList<>();
        
        for (int i = 0; i < arr.length; i++) {
            if (answer.isEmpty()) {
                answer.add(arr[i]);
            } else {
                int lastIdx = answer.size() - 1;
                if (answer.get(lastIdx) == arr[i]) {
                    answer.remove(lastIdx);
                } else {
                    answer.add(arr[i]);
                }
            }
        }
        
        if (answer.isEmpty()) {
            answer.add(-1);
        }
           
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}