import java.util.*;

class Solution {
    public int solution(String[] strArr) {
        Map<Integer, Integer> groupSizeCount = new HashMap<>();

        // 문자열 길이를 기준으로 그룹화하여 그룹 크기를 센다
        for (String str : strArr) {
            int length = str.length();
            groupSizeCount.put(length, groupSizeCount.getOrDefault(length, 0) + 1);
        }

        int maxGroupSize = 0;
        for (int size : groupSizeCount.values()) {
            maxGroupSize = Math.max(maxGroupSize, size);
        }

        return maxGroupSize;
    }
}