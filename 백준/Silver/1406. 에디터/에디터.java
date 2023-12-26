import java.util.*;
import java.lang.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        int n = Integer.parseInt(br.readLine());

        List<String> list = new LinkedList<>();
        for (String s : input.split("")) {
            list.add(s);
        }

        ListIterator<String> iterator = list.listIterator();
        while (iterator.hasNext()) {
            iterator.next();
        }
        
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String command = st.nextToken();

            switch (command) {
                case "P":
                    String str = st.nextToken();
                    iterator.add(str);
                    break;
                case "L":
                    if (iterator.hasPrevious()) {
                        iterator.previous();
                    }
                    break;
                case "D":
                    if (iterator.hasNext()) {
                        iterator.next();
                    }
                    break;
                case "B":
                    if (iterator.hasPrevious()) {
                        iterator.previous();
                        iterator.remove();
                    }
                    break;
            }
        }

        iterator = list.listIterator();
        StringBuilder answer = new StringBuilder();
        while (iterator.hasNext()) {
            answer.append(iterator.next());
        }

        System.out.println(answer.toString());
    }
}