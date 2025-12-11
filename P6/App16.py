def upperCase_Words(text):
    return " ".join(word.capitalize() for word in text.split())



print(upperCase_Words("hello world , i'm udaysinh"))