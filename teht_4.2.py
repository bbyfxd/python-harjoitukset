inchvalue = int(input("Enter the value in inch: "))
cmvalue = 2.54 * inchvalue

while True:
    inchvalue = int(input("Enter the value in inch: "))

    if inchvalue > 0:
        print('{}″ = {}cm'.format(inchvalue, cmvalue))
    elif inchvalue == 0:
        print('{}″ = {}cm'.format(inchvalue, cmvalue))


    else:
        print("End Program.")

