import java.util.*;

class Solution {
    public int solution(int[] rank, boolean[] attendance) {
        List<Integer> candidate = new ArrayList<>();
        for (int i = 0; i < rank.length; i++) {
            if (attendance[i]) {
                candidate.add(i);
            }
        }
        
        candidate.sort((a, b) -> rank[a] - rank[b]);
        System.out.println(candidate);
        int a = candidate.get(0);
        int b = candidate.get(1);
        int c = candidate.get(2);
        
        return 10000 * a + 100 * b + c;
    }
}