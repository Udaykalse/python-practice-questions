def count_vowels(s):

    vewels='aeiouAEIOU'
    Count=0
    for ch in s:

        if ch in vewels:

            Count+=1
    return Count



print(count_vowels("Developer"))

print('Hi')