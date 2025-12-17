def even_Number(lst):
    result=[]
    for x in lst:
        if x % 2 ==0:
            if x not in result:
                result.append(x)
    return result



print(even_Number([1,2,3,4,5,5,6,7,8,9,0,10,12,12,13]))