import java.util.*;

class Solution {
    public int solution(String str1, String str2) {
        str1 = str1.toLowerCase();
        str2 = str2.toLowerCase();

        List<String> set1 = generateMultiSet(str1);
        List<String> set2 = generateMultiSet(str2);
        
        // 공집합 처리
        if (set1.size() == 0 && set2.size() == 0) {
            return 65536;
        }

        // 정렬 후 교집합과 합집합을 구하는 부분
        List<String> intersectionList = new ArrayList<>();
        List<String> unionList = new ArrayList<>();
        
        // 교집합 구하기
        for (String s : set1) {
            if (set2.remove(s)) intersectionList.add(s);
        }
        
        unionList.addAll(set1);
        unionList.addAll(set2);

        double jaccard = (double) intersectionList.size() / (unionList.size() == 0 ? 1 : unionList.size());
        return (int)(jaccard * 65536);
    }

    private List<String> generateMultiSet(String str) {
        List<String> multiSet = new ArrayList<>();
        for (int i = 0; i < str.length() - 1; i++) {
            String s = str.substring(i, i + 2);
            if (s.chars().allMatch(Character::isLetter)) {
                multiSet.add(s);
            }
        }
        
        // 정렬
        Collections.sort(multiSet);
        return multiSet;
    }
}
