class Solution {
public:
    int longestValidParentheses(string s) {
        int open=0;
        int close=0;
        int maxSub=0;
        for(int i=0; i<s.size();i++){
            if(s[i]=='(')
                open++;
            else
                close++;
            if(open==close){
                maxSub=max(maxSub,2*open);
            }
            else if(close>open){
                open=close=0;
            }
        }
        open=close=0;
        for(int i=s.size()-1;i>=0;i--){
         if(s[i]==')')
                close++;
            else
                open++;
            if(open==close){
                maxSub=max(maxSub,2*close);  
            }
            else if(open>close)
                open=close=0;
        
    }
        return maxSub;
        }
};