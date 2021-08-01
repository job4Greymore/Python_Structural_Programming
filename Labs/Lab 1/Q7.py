from math import sqrt
def q7():

    # a = int(input("Enter A value:"))
    # b = int(input("Enter B value:"))
    # c = int(input("Enter C value:"))
    a, b, c = 3, 4, 5

    s = (a + b + c)/2

    num = sqrt(s*(s-a)*(s-b)*(s-c))

    print(num)

q7()