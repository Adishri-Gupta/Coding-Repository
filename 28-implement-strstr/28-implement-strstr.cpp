class Solution {
public:
    int strStr(string haystack, string needle) {
        int n=needle.size();
        string val;
     for(int i=0;i<haystack.size();i++){
         val=haystack.substr(i,n);
         if(val==needle)
             return i;
     }
        return -1;
    }
};