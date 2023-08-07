import java.util.*;

class Solution {
    public int[] solution(String[] keymap, String[] targets) {
        int[] answer = new int[targets.length];
        Map<Character, Integer> map = new HashMap<>();
        
        for (int i = 0; i < keymap.length; i++) {
            char[] keyChars = keymap[i].toCharArray();
            for (int j = 0; j < keyChars.length; j++) {
                char c = keyChars[j];
                if (map.containsKey(c)) {
                    map.put(c, Math.min(map.get(c), j + 1));
                } else {
                    map.put(c, j + 1);
                }
            }
        }
        
        for (int i = 0; i < targets.length; i++) {
            char[] targetChars = targets[i].toCharArray();
            for (char c : targetChars) {
                if (map.containsKey(c)) {
                    answer[i] += map.get(c);
                } else {
                    answer[i] = -1;
                    break;
                }
            }
        }
        
        return answer;
    }
}