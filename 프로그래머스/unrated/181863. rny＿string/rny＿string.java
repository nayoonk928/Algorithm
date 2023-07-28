import java.util.*;

class Solution {
    public String solution(String rny_string) {
        StringBuilder answer = new StringBuilder();
        char[] chars = rny_string.toCharArray();
        
        for (char ch : chars) {
            if (ch == 'm') {
                answer.append("rn");
            } else {
                answer.append(ch);
            }
        }
        
        return answer.toString();
    }
}