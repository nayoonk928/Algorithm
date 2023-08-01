import java.util.*;

class Solution {
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        int n = photo.length;
        int[] answer = new int[n];
        HashMap<String, Integer> map = new HashMap<>();
        
        for (int i = 0; i < name.length; i++) {
            map.put(name[i], yearning[i]);
        }
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < photo[i].length; j++) {
                String temp = photo[i][j];
                if (map.containsKey(temp)) {
                    answer[i] += map.get(temp);
                }
            }
        }
        
        return answer;
    }
}