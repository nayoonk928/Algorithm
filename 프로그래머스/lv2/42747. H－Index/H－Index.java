import java.util.*;

class Solution {
    public int solution(int[] citations) {
        int n = citations.length;
        int count = 0;
        
        Arrays.sort(citations);
        
        for (int i = citations[n - 1]; i >= 0; i--) {
            count = 0;
            for (int j = n - 1; j >= 0; j--) {              
                if (citations[j] > i) {
                    count++;
                }
            }
            
            if (count >= i) {
                return count;
            }
        }
        
        return count;
    }
}