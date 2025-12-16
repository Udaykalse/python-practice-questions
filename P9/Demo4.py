def missing_Invoice(nums):
    for i in range(nums[0],nums[-1]):
        if i not in nums:
            return i
        

print(missing_Invoice([1,2,3,4,6]))