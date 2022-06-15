a = float(input("Enter a: "))
b = float(input("Enter b: "))
if a > b:
    a = a + b
    b = a - b
    a = a - b
c = float(input("Enter c: "))
if b > c:
    b = b + c
    c = b - c
    b = b - c
    if a > b:
        a = a + b
        b = a - b
        a = a - b
print (a, "<", b, "<", c)

