def print_Binary(n):
    binary=""
    while n >0:
        binary = str(n % 2) + binary
        n //= 2
    return binary

n = int(input("Enter number: "))
print(print_Binary(n))