class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) / 2
        nums = sorted(nums)
        
        i = 0
        while i < len(nums):
            cnt = 0
            begin = nums[i]
            
            while i < len(nums):
                if begin == nums[i]:
                    cnt += 1
                    i += 1
                else:
                    break
            if cnt > n:
                return begin
            
        return 0