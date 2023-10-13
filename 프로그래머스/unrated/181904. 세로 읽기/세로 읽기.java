import java.util.*;

class Solution {
    public String solution(String my_string, int m, int c) {
        StringBuilder answer = new StringBuilder();
        char[] chars = my_string.toCharArray();
        
        for (int i = c - 1; i < chars.length; i += m) {
            answer.append(chars[i]);
        }
        
        return answer.toString();
    }
}