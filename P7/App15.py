def remove_Duplicates(s):
    return "".join(dict.fromkeys(s))

print(remove_Duplicates("programming"))