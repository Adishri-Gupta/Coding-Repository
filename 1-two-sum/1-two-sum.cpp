class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
       unordered_map <int,int> sum;
       for(int i = 0;i<nums.size();i++){
           int val=nums[i];
           int complement=target-val;
           auto it=sum.find(complement);
           if(it!=sum.end()){
            return {it->second, i};
               }
           sum[val]=i;
       }
        return {};
    }
};