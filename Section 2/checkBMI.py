w = int(input("your weight(kg)?"))
h = int(input("your height(cm)?"))
BMI = w/((h/100)**2)
print( "Your BMI", BMI)

if BMI < 16:
    print ("You're Severely underweight")
elif 16 < BMI <= 18.5:
    print ("You're Underweight")
elif 18.5 < BMI <= 25:
    print ("Congra, You're Normal ahihi")
elif 25 < BMI <= 30:
    print ("You're Overweight")
else:
    print ("huhu You're Obese")
