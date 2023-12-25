import java.util.*;
import java.lang.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine()); // 컴퓨터 수
        int m = Integer.parseInt(br.readLine()); // 컴퓨터 쌍의 수
        ArrayList<Integer>[] computers = new ArrayList[n + 1];
        boolean[] visit = new boolean[n + 1];

        for (int i = 1; i <= n; i++) {
            computers[i] = new ArrayList<Integer>();
        }

        for (int i = 0; i < m; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            computers[u].add(v);
            computers[v].add(u);
        }

        System.out.println(dfs(computers, visit, 1, 0));
    }

    private static int dfs(ArrayList<Integer>[] computers, boolean[] visit, int index, int count) {
        visit[index] = true;
        for (int computer : computers[index]) {
            if (!visit[computer]) {
                count = dfs(computers, visit, computer, count + 1);
            }
        }

        return count;
    }
}