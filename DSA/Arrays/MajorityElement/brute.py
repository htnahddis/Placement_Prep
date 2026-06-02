
def majorityElement(nums):

    n = len(nums) - 1

    for i in range(len(nums)):
        count = 0

        for j in range(len(nums)):

            if nums[i] == nums[j]:
                count+=1
        if count > n/2:
            return nums[i]
        

nums = [3,2,2,2,1]
major= majorityElement(nums)
print(major)


#this honestly gives time limit exceeded on leetcode 

