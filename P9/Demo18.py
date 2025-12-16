def is_Prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n %i==0:
            return True
    return True


print(is_Prime(7))