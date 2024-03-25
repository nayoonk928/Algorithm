import java.util.*;

class Solution {
    public long solution(int[] sequence) {
        long maxEndingHere = 0, maxSoFar = Long.MIN_VALUE;
        long maxEndingHereNeg = 0, maxSoFarNeg = Long.MIN_VALUE;
        
        for (int num : sequence) {
            maxEndingHere = Math.max(num, maxEndingHere + num);
            maxSoFar = Math.max(maxSoFar, maxEndingHere);
            
            maxEndingHereNeg = Math.max(-num, maxEndingHereNeg - num);
            maxSoFarNeg = Math.max(maxSoFarNeg, maxEndingHereNeg);
            
            long temp = maxEndingHere;
            maxEndingHere = maxEndingHereNeg;
            maxEndingHereNeg = temp;
        }
        
        return Math.max(maxSoFar, maxSoFarNeg);
    }
}
