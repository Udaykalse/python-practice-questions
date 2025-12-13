def count_Consonants(s):
    return sum(1 for c in s.lower() if c.isalpha() and c not in 'aeiou')



print(count_Consonants("Hello World"))