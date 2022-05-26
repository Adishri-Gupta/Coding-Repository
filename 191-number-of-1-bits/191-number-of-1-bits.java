public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
      int val =0;
      while(n!=0){
          val++;
          n=n&(n-1);
      }
    return val;
    }
}