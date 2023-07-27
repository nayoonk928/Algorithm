class Solution {
    public int solution(int n, String control) {
        char[] ch = control.toCharArray();
        
        for (int i = 0; i < ch.length; i++) {
            if (ch[i] == 'w') {
                n++;
            }
            
            if (ch[i] == 's') {
                n--;
            }
            
            if (ch[i] == 'd') {
                n += 10;
            }
            
            if (ch[i] == 'a') {
                n -= 10;
            }
        }
        
        return n;
    }
}