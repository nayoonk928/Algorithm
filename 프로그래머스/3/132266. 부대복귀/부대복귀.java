import java.util.*;

class Solution {
    static class Edge {
        int to;
        int weight;

        Edge(int to, int weight) {
            this.to = to;
            this.weight = weight;
        }
    }

    public int[] solution(int n, int[][] roads, int[] sources, int destination) {
        List<List<Edge>> graph = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int[] road : roads) {
            int from = road[0];
            int to = road[1];
            graph.get(from).add(new Edge(to, 1));
            graph.get(to).add(new Edge(from, 1));
        }

        int[] answer = new int[sources.length];
        Arrays.fill(answer, -1);

        Map<Integer, Integer> shortestPathFromDestination = new HashMap<>();

        // 목적지로부터 각 지점까지의 최단 거리를 미리 계산
        dijkstra(destination, graph, shortestPathFromDestination);

        // 각 부대원의 출발지에서 목적지까지의 최단 경로를 찾음
        for (int i = 0; i < sources.length; i++) {
            int source = sources[i];
            int shortestPath = shortestPathFromDestination.getOrDefault(source, -1);
            answer[i] = shortestPath;
        }

        return answer;
    }

    // 다익스트라 알고리즘을 이용하여 각 지점으로부터 목적지까지의 최단 거리를 계산
    private void dijkstra(int destination, List<List<Edge>> graph, Map<Integer, Integer> shortestPathFromDestination) {
        PriorityQueue<Edge> pq = new PriorityQueue<>(Comparator.comparingInt(e -> e.weight));
        pq.offer(new Edge(destination, 0));

        while (!pq.isEmpty()) {
            Edge edge = pq.poll();
            int to = edge.to;
            int weight = edge.weight;

            if (shortestPathFromDestination.containsKey(to)) {
                continue; // 이미 최단 거리가 계산된 경우 건너뜀
            }

            shortestPathFromDestination.put(to, weight);

            for (Edge neighbor : graph.get(to)) {
                int nextTo = neighbor.to;
                int nextWeight = weight + neighbor.weight;
                pq.offer(new Edge(nextTo, nextWeight));
            }
        }
    }
}
