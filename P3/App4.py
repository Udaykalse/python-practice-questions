def count_even(nums):
    c=0
    for n in nums:
        if n%2==0:
            c+=1
    return c


print(count_even([1,2,3,4,5,6,0]))