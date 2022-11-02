def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    BMI = weight / (height * height)
    print("BMI = " + str(BMI))

    if BMI < 18.5:
        print("User is underweight")
    elif 18.5 <= BMI <= 25.0:
        print("User has normal weight")
    else:
        print("User is overweight")


calculate_bmi(height=57, weight=1.73)
