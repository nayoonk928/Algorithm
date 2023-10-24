import java.util.*;

class Solution {
    public int[] solution(String[] intStrs, int k, int s, int l) {
        List<Integer> answer = new ArrayList<>();
        
        for (String str : intStrs) {
            int sub = Integer.parseInt(str.substring(s, s + l));
            if (sub > k) answer.add(sub);
        }
        
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}