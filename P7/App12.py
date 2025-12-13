def char_Frequency(s):
    freq={}
    for c in s:
        freq[c]=freq.get(c,0)+1
    return freq

print(char_Frequency("udaysinh Kalse"))