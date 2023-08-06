import java.util.*;

class Solution {
    public String solution(String[] survey, int[] choices) {
        StringBuilder answer = new StringBuilder();
        Map<Character, Integer> scores = new HashMap<>();
        int n = survey.length;
        
        for (int i = 0; i < n; i++) {
            int choice = choices[i];
            int score = Math.abs(choice - 4);
            if (choice >= 1 && choice <= 3) {
                char c = survey[i].charAt(0);
                scores.put(c, scores.getOrDefault(c, 0) + score);
            } else if (choice >= 5 && choice <= 7) {
                char c = survey[i].charAt(1);
                scores.put(c, scores.getOrDefault(c, 0) + score);
            } 
        }
        
        answer.append(getPersonalityType(scores, 'R', 'T'));
        answer.append(getPersonalityType(scores, 'C', 'F'));
        answer.append(getPersonalityType(scores, 'J', 'M'));
        answer.append(getPersonalityType(scores, 'A', 'N'));
        
        return answer.toString();
    }
    
    private char getPersonalityType(Map<Character, Integer> scores, char type1, char type2) {
        int score1 = scores.getOrDefault(type1, 0);
        int score2 = scores.getOrDefault(type2, 0);
        return score1 >= score2 ? type1 : type2;
    }
}