import java.util.*;

class Solution {
    public int solution(int[] arr1, int[] arr2) {
        int length1 = arr1.length;
        int length2 = arr2.length;
        
        if (length1 > length2) {
            return 1;
        } else if (length1 < length2) {
            return -1;
        } else {
            int sum1 = Arrays.stream(arr1).sum();
            int sum2 = Arrays.stream(arr2).sum();

            if (sum1 > sum2) {
                return 1;
            } else if (sum1 < sum2) {
                return -1;
            } else {
                return 0;
            }
        }
        
    }
}