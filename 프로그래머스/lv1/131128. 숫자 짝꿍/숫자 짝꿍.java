import java.util.*;

class Solution {
    public String solution(String X, String Y) {
        Map<Character, Integer> xMap = new HashMap<>();
        Map<Character, Integer> yMap = new HashMap<>();
        StringBuilder answer = new StringBuilder();
        
        for (char c : X.toCharArray()) {
            xMap.put(c, xMap.getOrDefault(c, 0) + 1);
        }
        
        for (char c : Y.toCharArray()) {
            yMap.put(c, yMap.getOrDefault(c, 0) + 1);
        }
        
        for (char i = '9'; i >= '0'; i--) {
            int minCount = Math.min(xMap.getOrDefault(i, 0), yMap.getOrDefault(i, 0));
            for (int j = 0; j < minCount; j++) {
                answer.append(i);
            }
        }
        
        if (answer.length() == 0) {
            return "-1";
        } else if (answer.charAt(0) == '0') {
            return "0";
        } else {
            return answer.toString();
        }
    }
}