package BFS_DFS;
import java.util.*;

public class DFS2 {
    public int solution(int[][] dots) {
        int answer = 0;
        int[] dotIndex = {0,1,2,3};
        HashSet<Integer[]> candidateIndexs = new HashSet<>();
        combination(0,candidateIndexs, "", dotIndex, new boolean[4]);
        Iterator<Integer[]> itr = candidateIndexs.iterator();
        while(itr.hasNext()){
            Integer[] next = itr.next();
            System.out.print(" | " + next[0]+","+next[1]);
        }
        return answer;
    }
    
    public void combination(int depth, HashSet<Integer[]> candidateIndexs, String candidateIndex,int[] dotIndex, boolean[] used){
        if (depth == 2){
            Integer[] candidate = Arrays.stream(candidateIndex.trim().split(" ")).map(Integer::parseInt).toArray(Integer[]::new);
            if(candidate[0] < candidate [1]){
                candidateIndexs.add(candidate);
            }
            return;
        }
        
        for (int i = 0 ; i<dotIndex.length ; i++){
            if(!used[i]){
                used[i] = true;
                combination(depth+1, candidateIndexs, candidateIndex+" "+dotIndex[i], dotIndex, used);
                used[i] = false;
            }
        }
    }

    public static void main(String[] args) {
        int[][] dots = {{1,2},{2,1},{3,4},{4,5}};
        new DFS2().solution(dots);
    }
}
