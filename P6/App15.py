def second_largest_Num_In_Array(arr):
    max1=max2=float('-inf')

    for num in arr:
        if num > max1:
            max2=max1
            max1=num
        elif num > max2 and num != max1:
            max2=num
    return max2



print(second_largest_Num_In_Array([1,2,3,4,5]))