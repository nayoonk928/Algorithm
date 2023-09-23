class Solution {
    public int solution(String binomial) {
        String[] parts = binomial.split(" ");
        int a = Integer.parseInt(parts[0]); 
        char op = parts[1].charAt(0); 
        int b = Integer.parseInt(parts[2]); 

        int result = 0;

        switch (op) {
            case '+':
                result = a + b;
                break;
            case '-':
                result = a - b;
                break;
            case '*':
                result = a * b;
                break;
            default:
                break;
        }

        return result;
    }
}