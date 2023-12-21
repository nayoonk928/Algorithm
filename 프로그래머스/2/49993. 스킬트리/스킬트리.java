import java.util.*;

class Solution {
    public int solution(String skill, String[] skill_trees) {
        int answer = 0;
        String[] skillArray = skill.split("");
        
        for (String skillTree : skill_trees) {
            String[] array = skillTree.split("");
            Stack<String> stack = new Stack<>();
            
            for (String s : array) {
                if (skill.contains(s)) {
                    stack.push(s);
                }
            }
            
            if (checkSkillTree(stack, skillArray)) answer++;
        }
        
        return answer;
    }
     
    private boolean checkSkillTree(Stack<String> stack, String[] skillArray) {
        if (stack.isEmpty()) return true;
        
        while (stack.size() > 1) {
            int current = Arrays.asList(skillArray).indexOf(stack.pop()); 
            int previous = Arrays.asList(skillArray).indexOf(stack.peek());
        
            if (current - previous != 1) {
                return false;
            }
        }
        
        if (Arrays.asList(skillArray).indexOf(stack.peek()) != 0) {
            return false;
        } else {
            return true;
        }
    }
}