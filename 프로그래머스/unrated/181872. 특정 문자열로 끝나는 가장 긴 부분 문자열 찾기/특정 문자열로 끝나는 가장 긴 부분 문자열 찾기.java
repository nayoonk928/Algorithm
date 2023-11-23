class Solution {
    public String solution(String myString, String pat) {
        int startIndex = myString.lastIndexOf(pat); // pat로 끝나는 가장 마지막 부분 문자열의 시작 인덱스

        return myString.substring(0, startIndex + pat.length());
    }
}