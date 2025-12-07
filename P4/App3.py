def count_vowels(s):
    v="aeiouAEIOU"
    c=0
    for ch in s:
        if ch in v:
            c+=1
    return c

print(count_vowels("Developer"))