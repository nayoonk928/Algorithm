import java.util.*;

class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;
        // 원하는 상품명과 개수를 저장하는 맵
        Map<String, Integer> wantMap = new HashMap<>();
        
        for (int i = 0; i < want.length; i++) {
            wantMap.put(want[i], number[i]);
        }
        
        for (int i = 0; i <= discount.length - 10; i++) {
            // 10일치의 할인 품목 포함한 배열 생성
            String[] temp = Arrays.copyOfRange(discount, i, i + 10);
            
            boolean isValid = true;
            for (int j = 0; j < want.length; j++) {
                // 배열을 리스트로 변환하여 원하는 품목의 개수 확인
                int count = Collections.frequency(Arrays.asList(temp), want[j]);
                if (count != wantMap.get(want[j])) {
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
