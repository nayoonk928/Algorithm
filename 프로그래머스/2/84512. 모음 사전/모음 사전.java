import java.util.*;

class Solution {
    static List<String> list;
    static String [] vowels = {"A", "E", "I", "O", "U"};
    
    public int solution(String word) {
        int answer = 0;
        list = new ArrayList<>();
        dfs("", 0);
        
        for (int i = 0; i < list.size(); i++) {
            if (word.equals(list.get(i))) {
                answer = i;
                break;
            }
        }
        
        return answer;
    }
    
    private void dfs(String str, int length) {
        list.add(str);
        if (length == 5) return;
        for (int i = 0; i < 5; i++) {
            dfs(str + vowels[i], length + 1);
        }
    }
}