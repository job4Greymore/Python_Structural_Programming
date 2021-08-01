def q4():

    #Write a program that converts seconds into hr,min,sec

    #Get user input
    numOfSecs = int(input("Enter the number of seconds: "))
    
    #formula used:
    hr = numOfSecs // 3600 
    min = numOfSecs % 3600 // 60
    sec = numOfSecs % 3600 % 60 

    print(f'{hr},{min},{sec}')

q4()