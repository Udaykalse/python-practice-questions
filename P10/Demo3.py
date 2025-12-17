def find_Target(lst,target):
    for x in lst:
        if x == target:
            return "Found"
    return "Not Found"

print(find_Target([3,6,9,2], 9))