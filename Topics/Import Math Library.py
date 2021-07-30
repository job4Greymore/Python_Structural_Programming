from math import sqrt, pow

#Value declaration
a, b, c = 6, 11, -35

#forumla provided
discrim = sqrt(pow(b, 2) - 4 * a * c)

#Variable assigned cause lazy to type
z = (-b + discrim) / (2 * a)
y = (-b - discrim) / (2 * a)

#Output
print("First root = ", z)
print("First root rounded = ", round(z))
print("Second root = ", y)
print("Second root rounded = ", round(y))