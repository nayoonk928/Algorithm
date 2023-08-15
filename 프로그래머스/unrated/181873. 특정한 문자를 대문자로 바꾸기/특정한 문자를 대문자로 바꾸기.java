class Solution {
    public String solution(String my_string, String alp) {
        StringBuilder sb = new StringBuilder();
        
        for (char c : my_string.toCharArray()) {
            if (Character.toString(c).equals(alp)) {
                sb.append(Character.toUpperCase(c));
            } else {
                sb.append(c);
            }
        }
        
        return sb.toString();
    }
}