class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            result = target - nums[i]
            if result in nums and nums.index(result) != i:
                return(nums.index(result),i)