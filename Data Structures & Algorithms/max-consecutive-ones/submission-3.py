class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count,max_count = 0,0
        
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                if count > max_count:
                    max_count = count
            else:
                count = 0

        return max_count