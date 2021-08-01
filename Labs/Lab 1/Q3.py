def q3():

    #Write a program that takes in a 3 digit integer and displays the sum and product of the digits. 
    # E.g. if the number is 123, the sum displayed is 6 and the product is also 6.

    #Get user input on the 3 digit variable
        
    #if asking for int only
    num = int(input("Enter a 3-digit number:"))
    num1= num // 100
    num2 = (num - (num1 * 100) ) // 10
    num3 = (num - (num1 * 100) - (num2 * 10))

    #verify numbers are correct
    print(num1,num2,num3)
    
    #formulas used for actions
    sum = num1 + num2 +num3
    product = num1 * num2 * num3
    
    #result print
    print(f'the sum is: {sum}, the product is: {product}')  

q3()