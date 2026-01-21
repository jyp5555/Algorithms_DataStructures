import java.util.*;

class Solution {
    public int solution(String[] s1, String[] s2) {
        int answer = 0;
        
        List<String> s2list = new ArrayList<>();
        s2list = Arrays.asList(s2);
        
        for (String s : s1){
            if (s2list.contains(s)) {
                answer += 1;
            }
        }
        
        return answer;
    }
}