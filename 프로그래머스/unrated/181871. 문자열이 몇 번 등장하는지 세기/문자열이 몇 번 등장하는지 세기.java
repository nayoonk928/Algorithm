class Solution {
    public int solution(String myString, String pat) {
        int answer = 0;
        int patLength = pat.length();
        int strLength = myString.length();

        for (int i = 0; i <= strLength - patLength; i++) {
            String subString = myString.substring(i, i + patLength);

            if (subString.equals(pat)) {
                answer++;
            }
        }

        return answer;
    }
}