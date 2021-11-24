Number=eval(input("Enter the athletes  Number"))
if type(Number)==int:
    if Number==1:
        print("Gold")
    elif Number==2:
        print("Silver")
    elif Number==3:
        print("Bronze")
    else:
        print("Thanks for participating")
else:
    print("Athletes Number should be an interger")
