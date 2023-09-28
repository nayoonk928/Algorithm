import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        int startIdx = -1;
        int endIdx = -1;

        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == 2) {
                startIdx = i;
                break;
            }
        }

        for (int i = arr.length - 1; i >= 0; i--) {
            if (arr[i] == 2) {
                endIdx = i;
                break;
            }
        }

        if (startIdx + endIdx < 0) {
            return new int[]{-1};
        }

        List<Integer> result = new ArrayList<>();
        for (int i = startIdx; i <= endIdx; i++) {
            result.add(arr[i]);
        }

        return result.stream().mapToInt(Integer::intValue).toArray();
    }
}
