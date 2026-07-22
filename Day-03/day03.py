# Operators in Python :- 

# 1- Arithmetic Operators :- (+, -, *, /, %, //, **)


a = 4
b = 6


print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b) # Modulus ( To calculate the remander)

print(33/4)

print(a//b) # Floor_division / Truncation (Divide and remove decimal part from answer)

print(5//2)

print(5**3) # Exponential (to calculate the power of a number 5**3 => 5*5*5= 125)

print(2**5)

# 2- Relational/Conditional Operator
#   > < >= <= == != (return boolean answer True/False)

a = 4
b = 2

print (a>b)
print (a<b)
print (a>=b)
print (a<=b)
print (a==b)
print (a!=b)


# 3- Assignment Operators

a = 10        # ( a is assign to 10)
a += 1        # => a = a+1
a *= 2        # =>  a = a*2

print (a)


# 4- Membership Operators        (Check existence)
#     in, not in    (Return Boolean Answer True/False


a = "aman"
b = "amankumar"
print (a in b)
print ("ankum" in b)
print ("ka" in b)
print ("ka" not in b)


a = [1,2,3]
b = [1,2,3]

print(a in b)

c = [1,2,[1,2,3],5]

print (a in c)

# 5- Identity Operator (check exact match)
#     is, is not (return boolean answer True/False)
    

a = "aman"
b = "amankumar"
c = "aman"

print (a is b)
print (a is c)

# 6- Logical Operators
#    and, or, not
# and:- If both condition are True, result is True
#       otherwise False.

print (10<3 and 10<55)
print (10<44 and 10<77)
print (10>44 and 10>77)



print (10<3 or 10<55)
print (10<44 or 10<77)
print (10>44 or 10>77)


print (not 10<55)
print (not 10<77)
print (not 10>77)


