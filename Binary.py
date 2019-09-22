decimal = int(input("Number in decimal format: "))

def binary(n):
    output = ""
    while n > 0:
        output = "{}{}".format(n % 2, output)
        n = n // 2
    return output

# our method
print(binary(decimal))

