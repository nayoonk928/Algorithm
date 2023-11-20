import java.util.*;

class Solution {
    public int[] solution(int[] arr, boolean[] flag) {
        ArrayList<Integer> X = new ArrayList<>();

        for (int i = 0; i < arr.length; i++) {
            if (flag[i]) {
                for (int j = 0; j < arr[i] * 2; j++) {
                    X.add(arr[i]);
                }
            } else {
                int size = X.size();
                for (int j = 0; j < arr[i]; j++) {
                    X.remove(size - 1 - j);
                }
            }
        }

        int[] result = new int[X.size()];
        for (int i = 0; i < X.size(); i++) {
            result[i] = X.get(i);
        }

        return result;
    }
}