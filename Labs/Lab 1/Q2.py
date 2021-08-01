def q2():

    #Write a program that reads 3 numbers and displays the sum and average of these 3 numbers.

    #Get user to input 3 numbers to the 3 variables.
    #if allow any number include dp
    num1 = float(input("Enter the first number:"))
    num2 = float(input("Enter the second number:"))
    num3 = float(input("Enter the third number:"))
    
    #if asking for int only
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number:"))
    num3 = int(input("Enter the third number:"))

    sum  = num1 + num2 + num3
    avg = sum/3 
    #Results with dp
    print(f'Sum of 3 numbers is {sum}, Average of 3 numbers is {avg}')
    #Results with no dp
    print(f'Sum of 3 numbers is {sum:.0f}, Average of 3 numbers is {avg:.0f}')

q2()