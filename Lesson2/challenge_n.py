"""
N.
Create a nested for loop to create X shape (width is 7, length is 7):

"""
lstcol = 7
for i in range (lstcol):
   for j in range(lstcol):
       if i == j or i+j == lstcol - 1:
           print("*", end = "")
       else:
           print (" ", end="")
   print()
