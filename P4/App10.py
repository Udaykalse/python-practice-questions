def is_Palindrome(s):
    s=s.replace(" ","").lower()
    return s==s[::-1]

print(is_Palindrome("madam"))