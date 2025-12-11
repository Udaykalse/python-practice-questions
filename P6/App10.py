def flat_Array(arr):
    import itertools
    resukt=[]
    def flatten(a):
        for i in a:
            if isinstance (i,list):
                flatten(i)
            else:
                resukt.append(i)
    flatten(arr)
    return resukt

print(flat_Array([1, [2, [3, [4]]]]))