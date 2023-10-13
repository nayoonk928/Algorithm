import java.util.*;

class Solution {
    public String[] solution(String my_string) {
        List<String> answer = new ArrayList<>();
        int len = my_string.length();
        
        for (int i = len - 1; i >= 0; i--) {
            answer.add(my_string.substring(i, len));
        }
        
        Collections.sort(answer);
        
        return answer.toArray(new String[0]);
    }
}