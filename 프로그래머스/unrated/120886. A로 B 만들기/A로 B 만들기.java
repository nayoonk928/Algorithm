import java.util.*;

class Solution {
    public int solution(String before, String after) {
        char[] beforeArray = before.toCharArray();
        char[] afterArray = after.toCharArray();
        
        // before의 순서를 바꾸기
        Arrays.sort(beforeArray);
        Arrays.sort(afterArray);
        
        // 바꾼 후의 before와 after 비교
        if (Arrays.equals(beforeArray, afterArray)) {
            return 1;
        } 
        
        return 0;
    }
}
