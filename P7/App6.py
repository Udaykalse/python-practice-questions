def reverse_Words(sentence):
    return " ".join(sentence.split()[::-1])


print(reverse_Words("Hello World Python"))