def polynomial(n, x):
    # n is the order
    a = []
    print('Enter {0} coefficients(from low order to high order):'.format(n+1))
    for i in range(n+1):
        a.append(float(input())) # input() return a str
    result = a[n]
    for i in range(n-1, -1, -1):
        result = result * x + a[i]
    return result


result = polynomial(5, 5.7)
print("The result is {0}".format(result))
