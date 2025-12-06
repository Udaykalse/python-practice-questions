def remove_duplicates(nums):
    seen=set()
    result=[]
    for n in nums:
        if n not in seen:
            result.append(n)
            seen.add(n)
    return result

print(remove_duplicates([1,2,2,3,1,4])) 