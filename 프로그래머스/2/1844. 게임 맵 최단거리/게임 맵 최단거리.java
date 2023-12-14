import java.util.*;

class Solution {
    // 노드 클래스 정의
    static class Node {
        int x;
        int y;
        int distance;

        public Node(int x, int y, int distance) {
            this.x = x;
            this.y = y;
            this.distance = distance;
        }
    }
    
    public int solution(int[][] maps) {
        int n = maps.length;
        int m = maps[0].length;

        // 방문 여부를 나타내는 배열
        boolean[][] visited = new boolean[n][m];
        
        // 상, 하, 좌, 우 이동을 나타내는 배열
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};

        // 시작점을 큐에 추가
        Queue<Node> queue = new LinkedList<>();
        queue.offer(new Node(0, 0, 1));
        visited[0][0] = true;

        // BFS 탐색
        while (!queue.isEmpty()) {
            Node current = queue.poll();

            // 상대 팀 진영에 도착한 경우 최단 거리 반환
            if (current.x == n - 1 && current.y == m - 1) {
                return current.distance;
            }

            // 상, 하, 좌, 우 이동
            for (int i = 0; i < 4; i++) {
                int nx = current.x + dx[i];
                int ny = current.y + dy[i];

                // 이동 가능한 위치이고 아직 방문하지 않은 경우 큐에 추가
                if (nx >= 0 && nx < n && ny >= 0 && ny < m && maps[nx][ny] == 1 && !visited[nx][ny]) {
                    queue.offer(new Node(nx, ny, current.distance + 1));
                    visited[nx][ny] = true;
                }
            }
        }

        // 상대 팀 진영에 도착할 수 없는 경우
        return -1;
    }
}