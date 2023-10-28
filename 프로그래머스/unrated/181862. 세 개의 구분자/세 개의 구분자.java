import java.util.*;

class Solution {
    public String[] solution(String myStr) {
        List<String> result = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        boolean empty = true;

        for (int i = 0; i < myStr.length(); i++) {
            char current = myStr.charAt(i);

            if (current == 'a' || current == 'b' || current == 'c') {
                if (sb.length() > 0) {
                    result.add(sb.toString());
                    sb.setLength(0);
                    empty = false;
                }
            } else {
                sb.append(current);
            }
        }

        if (sb.length() > 0) {
            result.add(sb.toString());
            empty = false;
        }

        if (empty) {
            return new String[]{"EMPTY"};
        } else {
            return result.toArray(new String[0]);
        }
    }
}