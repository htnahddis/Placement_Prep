class Solution(object):
    def twoSum(self, nums, target):
        memory = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in memory:
                return [memory[complement], i]

            memory[nums[i]] = i