#Data Type

# int = Whole number, exact <e.g 0, 1, 2 ,3 etc..> - Scalar & Immutable(cannot be overwritten)
# float = Decimal number, imprecise <e.g 0.5, 0.25, 0.125, etc..> - Scalar & Immutable(cannot be overwritten)
# str = String of characters, free text. - Sequence data type & Immutable(cannot be overwritten)
# ("a") = tuple container of data - Sequence data that is Immuntable(cannot be overwritten)
# ["b"] = list container of data - Sequence data that is mutable(can be overwritten)

# int() - int function 
score = int(input("Enter score: ")) #declares that the score variable is an integer character/value

# float() - float function
weight = float(input("Enter weight: ")) #declares that the weight variable is a number with a decimal value. 

#str() - str function
name = str(input("Please enter your name: ")) #declares that the name variable is a string data type that accepts all character.
print(name)

alist = ("a", "b", "c") #tuple ("a")
blist = ["a", "b", "c"] #list ["b"]

#type finder:
print(type(name))
print(type(weight))
print(type(score))
print(type(alist))
print(type(blist))