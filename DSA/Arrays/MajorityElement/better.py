def majorityElement(nums):

    n = len(nums) - 1
    hashmap = {}

    for i in nums:
        hashmap[i] = hashmap.get(i,0) + 1

    for key, value in hashmap.items():
        if value > n//2:
            return key

        

nums = [3,2,2,2,1]
major= majorityElement(nums)
print(major)