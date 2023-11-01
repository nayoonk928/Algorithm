class Solution {
    public String solution(String my_string, int[] indices) {
        StringBuilder result = new StringBuilder();
        boolean[] remove = new boolean[my_string.length()];

        for (int index : indices) {
            remove[index] = true;
        }

        for (int i = 0; i < my_string.length(); i++) {
            if (!remove[i]) {
                result.append(my_string.charAt(i));
            }
        }

        return result.toString();
    }
}