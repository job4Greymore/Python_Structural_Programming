def q6():
    #Get meal cost:
    costOfMeal = float(input("Enter meal amount($): "))
    #50% discount given:
    disc_50 = costOfMeal/2
    #10% service charge:
    serviceCharge = disc_50 * 0.10
    #7% gst charge after mealcost + service charge
    gst = (disc_50 + serviceCharge) * 0.07
    #totalAmount
    amountPayable = disc_50 + serviceCharge + gst
    #check if amountPayable correct
    # print(amountPayable) 

    #With formatting using .format(): #code $ had to be in line for result in line as well.
    print("Receipt")
    print("Cost of meal:   ${:>10,.02f}".format(costOfMeal))
    print("50% discount:   ${:>10,.02f}".format(disc_50))
    print("Service charge: ${:>10,.02f}".format(serviceCharge))
    print("GST(10%):       ${:>10,.02f}".format(gst))
    print("Total amount:   ${:>10,.02f}".format(amountPayable))

    #Without proper formatting using print(f''):
    print(f"Receipt \n Cost of meal: ${costOfMeal:>10,.02f}\n 50% Discount: ${disc_50:>10,.2f}\n Service charge: ${serviceCharge:>10,.2f}\n GST(10%): ${gst:>10,.2f}\n Total amount: ${amountPayable:>10,.2f}")

q6()