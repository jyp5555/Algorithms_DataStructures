
class Solution {
    public int solution(int n) {
        int answer = 0;
        int sqrtn = (int)Math.floor(Math.sqrt(n));
        for (int i=1; i <=sqrtn; i++){
            if (n % i == 0){
                answer += 1;
            }
        }
        if (sqrtn*sqrtn == n){
            answer = answer * 2 - 1;
        }else{
            answer = answer * 2;
        }
        
        return answer;
    }
}