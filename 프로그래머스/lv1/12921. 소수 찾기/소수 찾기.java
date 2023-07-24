import java.util.*;

class Solution {
    public int solution(int n) {
        int[] array = new int[n + 1];
        
        for (int i = 2; i <= n; i++) {
            array[i] = 1;
        }
        
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (array[i] == 0) continue;
            
            int num = i * 2;
            while (num <= n) {
                array[num] = 0;
                num += i;
            }
        }
        
        return Arrays.stream(array).sum();
    }
}