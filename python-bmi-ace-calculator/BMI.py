# BMI (Body Mass Index) Calculator

wieght_inp = int(input("Your wieght in KG (KiloGram) : "))
hieght_inp = float(input("Your hieght in meters : "))

sec = hieght_inp**2

bmi = wieght_inp/sec
print()
print("Your BMI is : ", end=" ")
print(bmi)
