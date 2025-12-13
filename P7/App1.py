def starts_ends(s,start,end):
    return s.startswith(start),s.endswith(end)

print(starts_ends("Hello World", "Hello", "World")) 