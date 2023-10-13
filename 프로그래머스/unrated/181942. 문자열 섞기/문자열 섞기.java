import java.util.*;

class Solution {
    public String solution(String str1, String str2) {
        StringBuilder answer = new StringBuilder();
        char[] chars1 = str1.toCharArray();
        char[] chars2 = str2.toCharArray();
        
        for (int i = 0; i < chars1.length; i++) {
            answer.append(chars1[i]);
            answer.append(chars2[i]);
        }
        
        return answer.toString();
    }
}