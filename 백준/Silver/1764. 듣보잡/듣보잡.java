import java.util.*;
import java.lang.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        
        String[] people = new String[n + m];
        for (int i = 0; i < people.length; i++) {
            people[i] = br.readLine();
        }

        solution(people);
    }

    public static void solution(String[] people) {
        int count = 0;
        Map<String, Integer> map = new TreeMap<>();
        
        for (String person : people) {
            map.put(person, map.getOrDefault(person, 0) + 1);
            if (map.get(person) > 1) {
                count++;
            }
        }

        System.out.println(count);
        for (Map.Entry<String, Integer> entry : map.entrySet()) {
            if (entry.getValue() > 1) {
                System.out.println(entry.getKey());
            }
        }
    }
}