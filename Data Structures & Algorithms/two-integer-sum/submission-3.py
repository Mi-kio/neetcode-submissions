class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # i = 0
        # j=i+1
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if nums[i]+nums[j] == target and i != j:
        #             return [i,j]
        #             break
        
        # return [-1,-1]

        dictt = {}
        for i in range(len(nums)):
            tw = target - nums[i]
            if tw in dictt:
                j = dictt[tw]
                if i > j: return [j,i]
                else: return [i,j]
            else:
                dictt[nums[i]] = i
        
        return []


        