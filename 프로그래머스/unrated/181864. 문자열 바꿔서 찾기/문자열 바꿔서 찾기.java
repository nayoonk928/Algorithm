import java.util.*;

class Solution {
    public int solution(String myString, String pat) {
        StringBuilder sb = new StringBuilder();
        char[] chars = myString.toCharArray();
        
        for (char ch : chars) {
            if (ch == 'A') {
                sb.append('B');
            } else {
                sb.append('A');
            }
        }
        
        if (sb.toString().contains(pat)) {
            return 1;
        } 
        
        return 0;
    }
}