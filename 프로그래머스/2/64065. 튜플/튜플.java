import java.util.*;

class Solution {
    public int[] solution(String s) {
        Map<String, Integer> map = new HashMap<>();
        String[] array = s.split(",|\\}|\\{");
        
        for (int i = 0; i < array.length; i++) {
            if (!array[i].matches("[0-9]+")) continue;

            map.put(array[i], map.getOrDefault(array[i], 0) + 1);
        }
        
        List<String> keySet = new ArrayList<>(map.keySet());
        keySet.sort((o1, o2) -> map.get(o2).compareTo(map.get(o1)));
        
        List<Integer> answer = new ArrayList<>();
        for (String key : keySet) {
            answer.add(Integer.valueOf(key));
        }
        
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}