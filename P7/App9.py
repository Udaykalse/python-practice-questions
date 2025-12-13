def extract_digits(s):
    return "".join(c for c in s if c.isdigit())

print(extract_digits("a1b2c3"))