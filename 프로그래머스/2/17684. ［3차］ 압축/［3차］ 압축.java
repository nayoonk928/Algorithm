import java.util.*;

class Solution {
    public int[] solution(String msg) {
        List<Integer> answer = new ArrayList<>();
        Map<String, Integer> map = new HashMap<>();

        int index = 1;
        int maxIndex = 27;

        for (char c = 'A'; c <= 'Z'; c++) {
            map.put(c + "", index++);
        }

        for (int i = 0; i < msg.length(); ) {
            int n = 1;
            while (i + n <= msg.length() && map.containsKey(msg.substring(i, i + n))) {
                n++;
            }

            String w = msg.substring(i, i + n - 1);
            answer.add(map.get(w));

            if (i + n <= msg.length()) {
                map.put(msg.substring(i, i + n), maxIndex++);
            }

            i += n - 1;
        }

        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}
