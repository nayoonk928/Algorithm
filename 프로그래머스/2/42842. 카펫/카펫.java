import java.util.*;

class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        
        for (int width = 3; width <= 5000; width++) {
            for (int height = 3; height <= width; height++) {
                if (brown == (width + height -2) * 2) {
                    if (yellow == width * height - brown) {
                        answer[0] = width;
                        answer[1] = height;
                        return answer;
                    }
                }
            }
        }
        
        return answer;
    }
}