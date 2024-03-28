import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(br.readLine());
        String str = br.readLine();

        List<String[]> wordList = new ArrayList<>();
        Set<String> set = new HashSet<>();

        for (int i = 1; i < N; i++) {
            for(int j = i + 1; j < N; j++) {
                String first = str.substring(0, i);
                String second = str.substring(i, j);
                String third = str.substring(j);
                wordList.add(new String[]{first, second, third});

                set.add(first);
                set.add(second);
                set.add(third);
            }
        }

        List<String> P = new ArrayList<>(set);
        Collections.sort(P);

        Map<String, Integer> map = new HashMap<>();
        int index = 1;
        for(String word : P) {
            map.put(word, index++);
        }

        int max = -1;
        for (String[] words : wordList) {
            int first = map.get(words[0]);
            int second = map.get(words[1]);
            int third = map.get(words[2]);

            max = Math.max(max, first + second + third);
        }
        System.out.println(max);
    }
}