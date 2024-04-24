import java.util.*;

public class Solution {
    public int[] solution(long[] numbers) {
        List<Integer> answerList = new ArrayList<>();

        for (long num : numbers) {
            String b = Long.toBinaryString(num); // 주어진 숫자를 이진수로 변환
            StringBuilder nodesBuilder = new StringBuilder(Integer.toBinaryString(b.length() + 1)); // 이진수 길이 + 1을 이진수로 변환
            
            // 포화 이진 트리가 아닌 경우 더미 노드(0)를 추가
            if (nodesBuilder.indexOf("1", 1) != -1) {
                int dummies = (1 << nodesBuilder.length()) - Integer.parseInt(nodesBuilder.toString(), 2);
                b = "0".repeat(dummies) + b;
            }
            
            // 이미 포화 이진 트리인 경우
            boolean result = dfs(b, b.length() / 2, (b.length() + 1) / 4);
            answerList.add(result ? 1 : 0);
        }

        // List를 int 배열로 변환
        int[] answer = new int[answerList.size()];
        for (int i = 0; i < answerList.size(); i++) {
            answer[i] = answerList.get(i);
        }

        return answer;
    }

    // DFS를 이용하여 이진 트리가 포화 이진 트리인지 확인하는 함수
    private boolean dfs(String b, int i, int depth) {
        if (depth == 0) { // 리프 노드에 도달했다면
            return true; // 포화 이진 트리
        }

        // 부모 노드가 '0'일 때
        // 왼쪽 자식 노드가 '1'이거나 오른쪽 자식 노드가 '1'이라면 포화 이진 트리가 될 수 없음
        else if (b.charAt(i) == '0') {
            if (b.charAt(i - depth) == '1' || b.charAt(i + depth) == '1') {
                return false;
            }
        }

        // 왼쪽 서브 트리 탐색
        boolean left = dfs(b, i - depth, depth / 2);
        // 오른쪽 서브 트리 탐색
        boolean right = dfs(b, i + depth, depth / 2);
        return left && right;
    }

}
