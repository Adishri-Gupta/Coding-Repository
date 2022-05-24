class Solution {
public:
    bool isMonotonic(vector<int>& nums) {
     int first=nums[0];
     int last=nums[nums.size()-1];
     if(first<last){
         for(int i=0;i<nums.size()-1;i++){
             if(nums[i]>nums[i+1])
                 return false;
         }
     }
    else if(first>last){
        for(int i=0;i<nums.size()-1;i++){
            if(nums[i]<nums[i+1])
                return false;
        }
    }
    else if(first==last){
        for(int i=0;i<nums.size()-1;i++){
            if(nums[i]!=nums[i+1])
                return false;
        }
    }
    return true;
    }
};