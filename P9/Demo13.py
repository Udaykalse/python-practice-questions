def common_Cust(a,b):
    return list(set(a) & set(b))


print(common_Cust([1,2,3],[2,3,4]))