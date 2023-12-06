import java.util.*;

class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;
        int n = want.length;
        Map<String, Integer> wantMap = new HashMap<>();
        
        for (int i = 0; i < n; i++) {
            wantMap.put(want[i], number[i]);
        }
        
        for (int i = 0; i <= discount.length - 10; i++) {
            String[] temp = Arrays.copyOfRange(discount, i, i + 10);

            Map<String, Integer> tempMap = new HashMap<>();
            for (String product : temp) {
                tempMap.put(product, tempMap.getOrDefault(product, 0) + 1);
            }

            boolean isValid = true;
            for (String key : wantMap.keySet()) {
                if (!tempMap.containsKey(key) || tempMap.get(key) != wantMap.get(key)) {
                    isValid = false;
                    break;
                }
            }

            if (isValid) {
                answer++;
            }
        }
        
        return answer;
    }
}