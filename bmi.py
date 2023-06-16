def calculate_bmi(height,weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi=weight/((height)**2)
    print(bmi)

    if bmi<18.5:
        print("Under Weight")
        return -1
    elif bmi>25.0:
        print("Over Weight")
        return 1
    else:
        print("Normal Weight")
        return 0

calculate_bmi(weight=55,height=1.74)
