def q9():
    #Getting number input from user
    # number = int(input("Enter seconds in integer: "))

    #forumla used:
    hr = int(input("Enter current hr: "))
    min = int(input("Enter Current min:"))
    sec = int(input("Enter current sec: "))
    print("Clock time is {:02d}:{:02d}:{:02d}".format(hr, min, sec))
    
    #convert Time into seconds (hr * 60 *60), (min *60)
    newTimeInSeconds = hr * 3600  + min * 60 + sec +1
    
    #compute back into format(hr, min, sec)
    
    # compute/extract to seconds
    new_Sec = newTimeInSeconds % 60
    # compute/extract to minutes
    new_Min = newTimeInSeconds // 60 % 60
    # compute/extract to hours
    new_Hr = newTimeInSeconds //3600 % 24

    #result
    print("After 1 second, the time is {:02d}:{:02d}:{:02d}".format(new_Hr, new_Min, new_Sec))

    #result using f string:
    print(f"after 1 second, the time is {new_Hr:02d}:{new_Min:02d}:{new_Sec:02d}")


q9()
