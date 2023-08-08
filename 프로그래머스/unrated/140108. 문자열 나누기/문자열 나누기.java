import java.util.*;

class Solution {
    public int solution(String s) {
        List<String> substrings = new ArrayList<>();
        
        while (!s.isEmpty()) {
            char x = s.charAt(0);
            int countX = 1;
            int countNonX = 0;
            
            for (int i = 1; i < s.length(); i++) {
                char currentChar = s.charAt(i);
                if (currentChar == x) {
                    countX++;
                } else {
                    countNonX++;
                }
                
                if (countX == countNonX) {
                    substrings.add(s.substring(0, i + 1));
                    s = s.substring(i + 1);
                    break;
                }
            }
            
            if (countX != countNonX) {
                substrings.add(s);
                break;
            }
        }
        
        return substrings.size();
    }
}