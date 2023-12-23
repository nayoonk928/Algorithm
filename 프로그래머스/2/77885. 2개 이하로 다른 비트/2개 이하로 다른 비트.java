import java.util.*;

class Solution {
    public long[] solution(long[] numbers) {
        long[] answer = new long[numbers.length];
        
        for (int i = 0; i < numbers.length; i++) {
            if (numbers[i] % 2 == 0) {
                answer[i] = numbers[i] + 1;
            } else {
                String numStr = Long.toBinaryString(numbers[i]);
                String nextStr = transformBinaryString(numStr);
                answer[i] = Long.parseLong(nextStr, 2);
            }
        }
        
        return answer;
    }
    
    private String transformBinaryString(String binaryString) {
        char[] binaryArray = binaryString.toCharArray();
        int lastIndex = binaryArray.length - 1;

        // 가장 오른쪽 0을 찾아 1로 변경
        for (int i = lastIndex; i >= 0; i--) {
            if (binaryArray[i] == '0') {
                binaryArray[i] = '1';
                // 바로 뒤의 1을 찾아 0으로 변경
                for (int j = i + 1; j <= lastIndex; j++) {
                    if (binaryArray[j] == '1') {
                        binaryArray[j] = '0';
                        break;
                    }
                }
                break; // 가장 오른쪽 0을 1로 변경 후 종료
            } else if (i == 0) {
                // 0이 없는 경우, 맨 앞에 1 추가하고 두 번째 자리를 0으로 변경
                binaryString = "1" + binaryString;
                binaryArray = binaryString.toCharArray();
                binaryArray[1] = '0';  // 두 번째 자리를 0으로 변경
                break;
            }
        }

        return new String(binaryArray);
    }
}