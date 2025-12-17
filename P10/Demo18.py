def remove_Duplicates(lst):
    result=[]
    for x in lst:
        if x not in result:
            result.append(x)
    return result


print(remove_Duplicates([1,2,2,3,1]))