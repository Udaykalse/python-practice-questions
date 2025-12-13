def longest_word(sentence):
    return max(sentence.split(),key=len)


print(longest_word("Python is amazing language"))