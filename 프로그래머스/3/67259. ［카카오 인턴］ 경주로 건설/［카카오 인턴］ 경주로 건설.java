import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

class Solution {
    private static final int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}}; // 상, 하, 좌, 우
    private static final int STRAIGHT = 100;
    private static final int CORNER = 500;

    public int solution(int[][] board) {
        int N = board.length;
        int[][][] cost = new int[N][N][4]; // 각 위치와 방향까지 고려한 최소 비용 저장
        for (int[][] layer : cost) {
            for (int[] row : layer) {
                Arrays.fill(row, Integer.MAX_VALUE); // 최소 비용을 무한대로 초기화
            }
        }

        Queue<Road> queue = new LinkedList<>();
        queue.add(new Road(0, 0, -1, 0)); // 출발점 추가
        for (int i = 0; i < 4; i++) {
            cost[0][0][i] = 0; // 시작점의 비용을 0으로 설정
        }

        while (!queue.isEmpty()) {
            Road current = queue.poll();

            for (int i = 0; i < 4; i++) {
                int nx = current.x + directions[i][0];
                int ny = current.y + directions[i][1];

                if (nx >= 0 && nx < N && ny >= 0 && ny < N && board[nx][ny] == 0) {
                    int newCost = current.cost + STRAIGHT;
                    if (current.direction != -1 && current.direction != i) {
                        newCost += CORNER;
                    }

                    if (cost[nx][ny][i] > newCost) {
                        cost[nx][ny][i] = newCost;
                        queue.add(new Road(nx, ny, i, newCost));
                    }
                }
            }
        }

        // 도착 지점에서의 최소 비용 계산
        return Arrays.stream(cost[N-1][N-1]).min().getAsInt();
    }

    static class Road {
        int x, y, direction, cost;

        Road(int x, int y, int direction, int cost) {
            this.x = x;
            this.y = y;
            this.direction = direction;
            this.cost = cost;
        }
    }
}
