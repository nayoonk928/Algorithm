import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        String[] strNums = Arrays.stream(numbers).mapToObj(String::valueOf).toArray(String[]::new);
        
        Arrays.sort(strNums, (s1, s2) -> (s2 + s1).compareTo(s1 + s2));
        
        String answer = String.join("", strNums);
        
        // answer가 "0"인 경우와 앞에 0이 여러 개 있는 경우 처리
        if (answer.length() > 0 && answer.charAt(0) == '0') {
            int i = 0;
            while (i < answer.length() && answer.charAt(i) == '0') {
                i++;
            }
            if (i == answer.length()) {
                // answer가 "000..."인 경우
                answer = "0";
            } else {
                // 앞에 0이 여러 개 있는 경우
                answer = answer.substring(i);
            }
        }

        return answer;
    }
}