import java.util.*;

class Solution {
    public int solution(int k, int m, int[] score) {
        int totalAppleCount = score.length;

        if (totalAppleCount < m) {
            return 0;
        }

        int boxNum = totalAppleCount / m;

        Arrays.sort(score);

        int answer = 0;
        int startIndex = totalAppleCount - m;
        for (int i = 0; i < boxNum; i++) {
            answer += score[startIndex] * m;
            startIndex -= m;
        }

        return answer;
    }
}
