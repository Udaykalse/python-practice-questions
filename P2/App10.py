def largest(arr):
    return max(arr) , min(arr)

print (largest([1,2,3,4,5]))

print('---------------------Remove Duplicates ------------------------')
def remove_Duplicate(arr):
    return list(set(arr))


print(remove_Duplicate([1,2,2,3,1,2,3,4]))


print('----------------------Prime or Not -----------------------')

def is_Prime(n):
    if n<2:
        return False
    for i in range (2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

print(is_Prime(11))


print('----------------------Merge Two Lists -----------------------')

def merege_List(a,b):
    return a+b
print(merege_List([1,2],[3,4]))