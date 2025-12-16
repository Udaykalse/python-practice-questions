def vowel_Count(name):
    return sum(1 for c in name.lower() if c in 'aeiou')


print(vowel_Count('Udaysinh Kalse'))