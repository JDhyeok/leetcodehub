class Solution {
    public int searchInsert(int[] nums, int target) {
        int l = 0;
        int r = nums.length;
        int mid = 0;
        
        if(nums[r - 1] < target)
            return r;
        
        while(l <= r) {
            mid = (l + r) / 2;
            
            if(nums[mid] < target){
                l = mid + 1;
            }
            else if(nums[mid] > target){
                r = mid - 1;
            }
            else{
                return mid;
            }
            
        }
        
        if(nums[mid] < target)
            return mid + 1;
        else
            return mid;
    }
}