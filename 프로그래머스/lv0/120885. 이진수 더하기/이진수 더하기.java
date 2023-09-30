class Solution {
    public String solution(String bin1, String bin2) {
        StringBuilder answer = new StringBuilder();
        int carry = 0;

        int i = bin1.length() - 1;
        int j = bin2.length() - 1;

        while (i >= 0 || j >= 0 || carry > 0) {
            int num1 = (i >= 0) ? bin1.charAt(i) - '0' : 0;
            int num2 = (j >= 0) ? bin2.charAt(j) - '0' : 0;

            int sum = num1 + num2 + carry;
            answer.insert(0, sum % 2);
            carry = sum / 2;

            i--;
            j--;
        }

        return answer.toString();
    }
}