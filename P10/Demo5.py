def Count_Even_Odd(lst):
    even=odd=0
    for x in lst:
        if x %2 == 0:
            even+=1
        else:
            odd+=1
    return even,odd


print(Count_Even_Odd([1,2,3,4,5,6,7,8,9,0]))