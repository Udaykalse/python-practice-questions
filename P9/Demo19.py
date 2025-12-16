def strong_Password(pwd):
    return any(c.isdigit() for c in pwd) and any(c.isupper() for c in pwd)

print(strong_Password("Pass123"))