package BFS_DFS;

import java.util.*;
public class DFS{

    public void solution(){
        
        String[] words = {"A","B","C","D"};
        ArrayList<String> validWords = new ArrayList<>();

        permute(words, validWords, new boolean[4], 0, "");
    }

    private void permute(String[] words, ArrayList<String> validWords, boolean[] used,int depth, String currentWord){
        if (depth > 0){
            validWords.add(currentWord);
            System.out.println(validWords);
        }
        if (depth == 4){
            return;
        }

        for(int i = 0; i < words.length ; i++){
            if(!used[i]){
                used[i] = true;
                permute(words, validWords, used, depth+1, currentWord+words[i]);
                used[i] = false;
            }
        }
    }
    public static void main(String[] args){
        new DFS().solution();
    }
}