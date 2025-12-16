def product_Frequency(products):
    freq={}
    for p in products:
        freq[p]=freq.get(p,0)+1
    return freq

print(product_Frequency(["phone","laptop","phone"]))