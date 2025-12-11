def flatten(arr):
    result=[]
    for itM in arr:
        if isinstance(itM,list):
            result.extend(flatten(itM))
        else:
            result.append(itM)
    return result

print(flatten([1, [2, [3, [4]]]]))