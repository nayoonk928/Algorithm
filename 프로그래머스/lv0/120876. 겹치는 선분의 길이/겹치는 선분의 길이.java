import java.util.*;

class Solution {
    public int solution(int[][] lines) {
        int answer = 0;
        List<int[]> points = new ArrayList<>();
        
        for (int[] line : lines) {
            points.add(new int[]{line[0], 1});
            points.add(new int[]{line[1], -1});
        }
        
        Collections.sort(points, (a, b) -> a[0] != b[0] ? a[0] - b[0] : b[1] - a[1]);
        
        int count = 0;
        int prevPoint = points.get(0)[0];
        
        for (int[] point : points) {
            if (count >= 2) {
                answer += point[0] - prevPoint;
            }
            if (point[1] == 1) {
                count++;
            } else {
                count--;
            }
            if (count >= 2) {
                prevPoint = point[0];
            } else if (point[1] == -1) {
                prevPoint = point[0] + 1;
            }
        }
        
        return answer;
    }
}