class Solution {
    public String solution(String n_str) {
        char[] chars = n_str.toCharArray();
        
        int index = 0;
        while (index < chars.length && chars[index] == '0') {
            index++;
        }
        
        return n_str.substring(index);
    }
}