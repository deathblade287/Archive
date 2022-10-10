# ACE (Annual Ciggarete expense)

M = int(input("Number of cigarettes smoked per day : "))
C = int(input("Number of cigarettes in a pack : "))
P = int(input("Price per pack (INR) : "))

monthly = ((M / C) * 30) * P
annualy = ((M / C) * 365) * P

print('\n', "The monthly ACE is : ", end=" ")
print(monthly, '\n')
print("The annual ACE is : ", end=" ")
print(annualy)
