#Arithmetic Operators
x = 5
y = 2
str1 = "I love BD"
str2 = "555"
str3 = "555"

print("Test 1")

#Precedence from highest to lowest
t1 = x**y #x raised to power of y 
t2 = x%y #find remainder of x divided by y
t3 = x//y # x divided by y result return int()
t4 = x/y # x dived by y
t5 = x*y # x multiply y
t6 = x-y # x minus y
t7 = x+y # x plus y

print(t1,t2, t3, t4, t5, t6, t7)

print("Test 2")
# st1 = str1**y #Will fail as arthmetic operation not possible with str data type
# st2 = str1%y #Will fail as arthmetic operation not possible with str data type
# st3 = str1//y #Will fail as arthmetic operation not possible with str data type
# st4 = str1/y #Will fail as arthmetic operation not possible with str data type
st5 = str1*y 
print("st5 passed!")
# st6 = str1-y #Will fail as arthmetic operation not possible with str data type
#st7 = str1+y #Will fail as arthmetic operation not possible with str data type


print("Test 3") #string with string arithmetric operations
# nSt1 = str2**y #Will fail as arthmetic operation not possible with str data type
# nSt2 = str2%y #Will fail as arthmetic operation not possible with str data type
# nSt3 = str2//y #Will fail as arthmetic operation not possible with str data type
# nSt4 = str2/y #Will fail as arthmetic operation not possible with str data type
nSt5 = str2*y 
print("st5 passed!", nSt5) #notice the result it does not have spacing.

# nSt6 = str2-y #Will fail as arthmetic operation not possible with str data type
# nSt7 = str2+y  #can only concatenate(+) str to str data type.

print("Test 4") #string with string arithmetric operations
# ststr1 = str1**str2  #Wrong operation type
# ststr2 = str1%str2 #not all arguments converted during string format
# ststr3 = str1//str2 #Wrong operation type
# ststr4 = str1/str2 #Wrong operation type
# ststr5 = str1*str2 #Wrong operation type cannot multiply str with non-int type
# ststr6 = str1-str2 #Wrong operation type
ststr7 = str1+str2
print("ststr7 passed!", ststr7) #notice the result it does not have spacing.

