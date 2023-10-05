class Solution {
    public int solution(int[][] dots) {
        int xMin = Integer.MAX_VALUE;
        int xMax = Integer.MIN_VALUE;
        int yMin = Integer.MAX_VALUE;
        int yMax = Integer.MIN_VALUE;

        for (int[] dot : dots) {
            int x = dot[0];
            int y = dot[1];
            
            xMin = Math.min(xMin, x);
            xMax = Math.max(xMax, x);
            yMin = Math.min(yMin, y);
            yMax = Math.max(yMax, y);
        }

        int width = xMax - xMin;
        int height = yMax - yMin;
        int area = width * height;

        return area;
    }
}