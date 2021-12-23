class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> hashmap;
        
        for(int i = 0; i<nums.size() ; i++){
            if(hashmap.count(target-nums[i])){
                return {i,(hashmap[target-nums[i]])};
            }
            hashmap[nums[i]] = i;
        }
        return {};
    }
};