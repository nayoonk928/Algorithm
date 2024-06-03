class Solution {
    public static String solution(String my_string, int[][] queries) {
        StringBuilder sb = new StringBuilder(my_string);
        
        for (int[] query : queries) {
            int s = query[0];
            int e = query[1];
            reverseSubstring(sb, s, e);
        }
        
        return sb.toString();
    }

    private static void reverseSubstring(StringBuilder sb, int s, int e) {
        while (s < e) {
            char temp = sb.charAt(s);
            sb.setCharAt(s, sb.charAt(e));
            sb.setCharAt(e, temp);
            s++;
            e--;
        }
    }
}
