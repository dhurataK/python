def multiply(a,b):
    for i in range(0, len(a)):
        a[i] *= b
    return a
a = [ 2, 4, 10, 16 ]
b = multiply(a, 5)
print b
