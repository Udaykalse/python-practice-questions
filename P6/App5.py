def merge_Two_Sorted(a,b):
    i=j=0
    result=[]
    while i < len(a) and j<len(b):
        if a[i]<b[j]:
            result.append(a[i])
            i+=1
        else:
            result.append(b[j])
            j+=1
    return result+a[i:]+b[j:]





print(merge_Two_Sorted([1,3,5], [2,4,6]))