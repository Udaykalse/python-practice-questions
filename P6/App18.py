def flatten(arr):
    result=[]
    for itm in arr:
        if isinstance(itm,list):
            result.extend(flatten(itm))
        else:
            result.append(itm)
    return result



print(flatten([1, [2, [3, [4]]]]))