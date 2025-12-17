def is_Eligible(age):
    if age < 18:
        return "Not Eligible"
    return "Eligible"


print(is_Eligible(19))