import java.util.*;

class Solution {
    public int[] solution(int[] arr, int[] delete_list) {
        List<Integer> list = new ArrayList<>();
        boolean isDeleted;
        
        for (int i = 0; i < arr.length; i++) {
            isDeleted = false;
            
            for (int j = 0; j < delete_list.length; j++) {
                if (arr[i] == delete_list[j]) {
                    isDeleted = true;
                    break;
                }
            }
            
            if (!isDeleted) {
                list.add(arr[i]);
            }
        }
        
        return list.stream().mapToInt(Integer::intValue).toArray();
    }
}