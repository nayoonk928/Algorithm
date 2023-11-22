class Solution {
    public String solution(String my_string, int s, int e) {
        StringBuilder reversedSubstring = new StringBuilder(my_string.substring(s, e + 1));

        reversedSubstring.reverse();

        return my_string.substring(0, s) + reversedSubstring + my_string.substring(e + 1);
    }
}