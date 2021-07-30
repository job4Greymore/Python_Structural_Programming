#Type conversion

n1, n2 = 3, 4.0

sum = n1 + n2
print(sum) # notice that the result converts into a decimal value.

sum2 = n1 + int(n2)
print(sum2) #notice that the conversion of the decimal to int has result in an integer value.