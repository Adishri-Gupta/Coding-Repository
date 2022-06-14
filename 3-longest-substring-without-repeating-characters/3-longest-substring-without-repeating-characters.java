class Solution {
    public int lengthOfLongestSubstring(String s) {
        int[] charCount =  new int[128];
        
        int i=0;
        int j=0;
        int res=0;
        
        while(j<s.length()){
            char valR=s.charAt(j);
            charCount[valR]++;
            
            while(charCount[valR]>1){
             char valL=s.charAt(i);
             charCount[valL]--;
             i++;
            }
            res=Math.max(res,j-i+1);
            j++;
        }   
        return res;
    }
}