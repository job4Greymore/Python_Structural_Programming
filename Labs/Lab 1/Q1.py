def q1():

    #c = centigrade, f = fahrenheit
    
    f = float(input("Enter temperature in Fahrenheit: "))
    #Formula for centigrade
    c= 5/9*(f-32)

    print(f'{f:.2f} fahrenheit is coverted to {c:.2f}centigrade')

q1()