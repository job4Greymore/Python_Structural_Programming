def q8():
    #l = Loan, i = interest, n = duration
    l = float(input("Enter your loan amount: "))
    i = float(input("Enter your interest rate of your loan amount: "))
    n = float(input("Enter your loan duration: "))
 
    #c = compute compound interest 
    compoundInterest = l * (1 + i/100)**n

    #display compound Interest
    print(f"Your coompound interest is ${compoundInterest:,.2f}")

q8()