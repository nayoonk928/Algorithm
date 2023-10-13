import java.util.*;

class Solution {
    public String solution(String my_string) {
        String lowerStr = my_string.toLowerCase();
        char[] chars = lowerStr.toCharArray();
        
        Arrays.sort(chars);
        
        StringBuilder answer = new StringBuilder();
        for (char c : chars) {
            answer.append(c);
        }
        
        return answer.toString();
    }
}