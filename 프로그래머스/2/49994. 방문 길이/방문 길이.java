import java.util.*;

class Solution {
    public int solution(String dirs) {
        int answer = 0;
        int currY = 5, currX = 5;
        boolean[][] w = new boolean[11][11];
        boolean[][] h = new boolean[11][11];
        
        for (char c : dirs.toCharArray()) {
            switch (c) {
                case 'U':
                    if (currY <= 0) continue;
                    
                    currY--;
                    if (!h[currY][currX]) {
                        h[currY][currX] = true;
                        answer++;
                    }
                    break;
                case 'D':
                    if (currY >= 10) continue;
                    
                    if (!h[currY][currX]) {
                        h[currY][currX] = true;
                        answer++;
                    }
                    
                    currY++;
                    break;
                case 'R':
                    if (currX >= 10) continue;
                    
                    if (!w[currY][currX]) {
                        w[currY][currX] = true;
                        answer++;
                    }
                    currX++;
                    break;
                case 'L':
                    if (currX <= 0) continue;
                    
                    currX--;
                    if (!w[currY][currX]) {
                        w[currY][currX] = true;
                        answer++;
                    }
                    break;
            }
        }
        
        return answer;
    }
}