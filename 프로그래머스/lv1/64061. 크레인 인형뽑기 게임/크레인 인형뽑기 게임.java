import java.util.*;

public class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < moves.length; i++) {
            boolean character = false; // 인형이 있으면 true
            int index = 0; // board에서 몇 번째 row에 인형이 있는지

            // moves[i]-1번째 column에 인형이 있는지 찾기
            for (int j = 0; j < board.length; j++) {
                if (board[j][moves[i] - 1] != 0) {
                    character = true;
                    index = j;
                    break;
                }
            }

            if (character) {
                if (!stack.isEmpty() && stack.peek() == board[index][moves[i] - 1]) {
                    stack.pop();
                    answer += 2;
                } else {
                    stack.push(board[index][moves[i] - 1]);
                }
                board[index][moves[i] - 1] = 0;
            }
        }
        return answer;
    }
}
