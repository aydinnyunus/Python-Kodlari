def fibonacci(n, output=[]):
    a=1
    b=1
    for i in range(n):
        a, b = b, a + b
        output.append(str(a))
    return output

number = int(input("Length of fibonacci sequence: "))

print("Result: 1,{}".format(",".join(fibonacci(number))))
