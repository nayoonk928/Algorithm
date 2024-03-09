import java.util.*;

class Solution {
    public String solution(String s) {
        StringBuilder answer = new StringBuilder();
        StringTokenizer st = new StringTokenizer(s, " ", true);
        
        while (st.hasMoreTokens()) {
            String token = st.nextToken();
            if (token.equals(" ")) {
                answer.append(" ");
                continue;
            }
            
            int cnt = 0;
            for (char c : token.toCharArray()) {
                if (cnt % 2 == 0) {
                    answer.append(Character.toUpperCase(c));
                } else {
                    answer.append(Character.toLowerCase(c));
                }
                cnt++;
            }
            
        }
        
        return answer.toString();
    }
}
