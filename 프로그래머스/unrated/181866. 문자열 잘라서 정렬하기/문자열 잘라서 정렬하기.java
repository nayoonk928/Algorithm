import java.util.*;

class Solution {
    public String[] solution(String myString) {
        String[] splits = myString.split("x");

        List<String> nonEmptyParts = new ArrayList<>();
        for (String split : splits) {
            if (!split.isEmpty()) {
                nonEmptyParts.add(split);
            }
        }

        String[] answer = nonEmptyParts.toArray(new String[0]);
        
        Arrays.sort(answer);
        
        return answer;
    }
}