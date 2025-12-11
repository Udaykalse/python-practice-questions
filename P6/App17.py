def add(a):
    def b_fun(b):
        return a+b
    return b_fun


print(add(2)(3))