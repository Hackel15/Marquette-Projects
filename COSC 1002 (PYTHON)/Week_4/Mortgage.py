def mortgage():
    print(40*"*")
    print("** The Ultimate Mortgage Calculator **")
    print(40*"*")
    principal = float(input("What is the principal: "))
    interest = float(input("What is the interest rate (in percents): "))/1200
    #print("Your minimum rate is ", interest*principal)
    print("{}, ${:.2f}".format("Your minimum rate is",interest*principal))
    payment = float(input("What is the monthly payment: "))
    month = 0
    #print("Month\tInterest\t\tRemaining Balance")
    print("{:<15}{:<15}{:<15}".format("Month","Interest","Remaining Balance"))

    while principal > 0:
        intpaid = principal*interest
        principal = principal + principal*interest - payment
        if principal < 0:
            lastpayment = payment + principal
            principal = 0
        month += 1
        #print(month,"\t",intpaid,"\t",principal)
        print("{:<15}${:<15.2f}${:<15.2f}".format(month,intpaid,principal))
    #print("You paid of the loan in", (month),", and your last payment was ", lastpayment)     
    print("{}{}{}${:.2f}".format("You paid of the loan in, ",month," and your last payment was ",lastpayment))
