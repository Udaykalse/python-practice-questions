def _is_Anagram(s1,s2):
    return sorted(s1.replace(" ","").lower())==sorted(s2.replace(" ","").lower())

print(_is_Anagram("Madam","AdamM"))