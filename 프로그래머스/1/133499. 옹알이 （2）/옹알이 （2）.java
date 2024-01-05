import java.util.*;

class Solution {
    public int solution(String[] babbling) {
        int answer = 0;

        for (String s : babbling) {
            if (canSpeak(s, "")) {
                answer++;
            }
        }

        return answer;
    }

    private boolean canSpeak(String s, String prev) {
        int len = s.length();
        if (len < 2) return false;

        if (len == 2) {
            return checkTwoChars(s, prev);
        }

        if (len == 3) {
            return checkThreeChars(s, prev);
        }

        if (checkTwoChars(s.substring(0, 2), prev)) {
            return canSpeak(s.substring(2), s.substring(0, 2));
        }

        if (checkThreeChars(s.substring(0, 3), prev)) {
            return canSpeak(s.substring(3), s.substring(0, 3));
        }

        return false;
    }

    private boolean checkTwoChars(String s, String prev) {
        if (s.equals(prev) || s.equals(prev)) {
            return false;
        } 
        
        return "ye".equals(s) || "ma".equals(s);
    }

    private boolean checkThreeChars(String s, String prev) {
        if (s.equals(prev) || s.equals(prev)) {
            return false;
        } 
        
        return "aya".equals(s) || "woo".equals(s);
    }
}
