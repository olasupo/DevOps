"""

Create a nested for loop (loop inside another loop) to create a pyramid shape:
"""

count = 5
for i in range(count):
  spc= (count -1 - i) * ' '
  print(spc, end=' ')
  for j in range(count):
    if i==5:
      break
    else:
      stra= (2*i+1)*"*"
      print(stra)
      break
