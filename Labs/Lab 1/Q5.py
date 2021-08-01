def q5():

    #write a program is able to sort coins apart, 50cents, 10cents, 5cents, 1cents

    #Get user input
    # num = int(input("Enter amount of cents: "))
    num = 97

    #num of 50cents
    cent_50  = num // 50

    #num of 10cents
    cent_10 = num % 50 // 10

    #num of 5cents
    cent_5 = num % 50 % 10 // 5

    #num of 1cents
    cent_1 = num % 50 % 10 % 5

    print(f'50 cents:{cent_50}, 10 cents: {cent_10}, 5 cents:{cent_5}, 1 cents: {cent_1}') 



q5()