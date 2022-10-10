#!/usr/bin/env python
# coding: utf-8

import numpy as np
print("Author: Georgios Koliou\nContact: georgios.koliou@gmail.com\n")


D = str(input("\n\n Do you want to save this? Type Y for Yes or N for No: "))


if D == "Y":
    F = str(input(
        "\n(The file's name must be [name_file].doc -> Word file or [name_file].txt -> Text file): "))
    file = open(F, "w")
else:
    print("\nOk! Nothing to save!")


if D == "Y":
    file.write("Author: Georgios Koliou\nContact: georgios.koliou@gmail.com\n\n")
else:
    print("")


R = int(input("\nGive number of rows: "))
C = int(input("\nGive number of columns: "))


if R == C:
    print("\nInsert the elements of the matrix A separated by space: ")
    numeri = list(map(int, input().split()))
elif D == 'Y':
    file.close()
    print("\n\nThe matrix is not square! It size is", R, "x", C, "\n\n")
    input("Press ENTER to exit and delete the file")
    import os
    os.remove(F)
    import sys
    sys.exit("AGAIN")
else:
    print("\n\nThe matrix is not square! It's siaze is", R, "x", C, "\n\n")
    input("Press ENTER to exit")
    import sys
    sys.exit("AGAIN")

matrice = np.array(numeri).reshape(R, C)
print("\nThe matrix of the linear equations is:\n\n", matrice,)
if D == "Y":
    file.write("\n\nThe matrix of the linear equations is:\n\n")
    file.write(str(matrice))
else:
    print("")


Rb = int(input("\nGive number of rows of column b:\n"))

if Rb == C:
    print("\nInsert the elements of row b separated by space:\n")
elif D == 'Y':
    file.close()
    print("The number of rows of vector b must be equals with number of column of matrix A,",
          Rb, "is not equals to", C,)
    input("Press ENTER to exit and delete the file")
    import os
    os.remove(F)
    import sys
    sys.exit("AGAIN")
else:
    print("\n\nVector b has not the right size..\n\n")
    input("Press ENTER to exit")
    import sys
    sys.exit("AGAIN")

b = list(map(int, input().split()))
bm = np.array(b).reshape(Rb, 1)

print("\nVector b is equals to:\n\n", bm,)

if D == "Y":
    file.write('\n\nVector b is equals to:\n\n')
    file.write(str(bm))
else:
    print("")


x = int(input("\nNumber of variables: "))

if x == R:
    print("\nInsert variables separated by space: ")
elif D == 'Y':
    file.close()
    print("Number of variables is not right..")
    input("Press ENTER to exit and delete the file")
    import os
    os.remove(F)
    import sys
    sys.exit("AGAIN")
else:
    print("\n\nVector x has not the right size..\n\n")
    input("Press ENTER to exit")
    import sys
    sys.exit("AGAIN")

var = list(map(str, input().split()))
var1 = np.array(var).reshape(x, 1)
print("\nVector x is equals to:\n\n", var1,)

if D == "Y":
    file.write('\n\nVector x is equals to:\n\n ')
    file.write(str(var1))
else:
    print("")


x = np.linalg.solve(matrice, bm)
sol = zip(var, x)
print("\nThe solutions of the Linear Equation System are:\n\n", list(sol),)

if D == "Y":
    file.write('\n\nThe solutions of the Linear Equation System are:\n\n')
    file.write(str(x))
    file.close()
else:
    print("")


input('\n\n\nPress ENTER to exit')
