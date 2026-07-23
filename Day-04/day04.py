# Python Operators
# 6- Logical Operator (return boolean value True/False)
# and , or , not

print( int(True) )
print( int(False) )
print( bool(1) )
print( bool(0) )
print( bool(3466) )
print( bool(-734567) )
print( bool('aman kumar') )
print( bool(False) )
print( bool('False') )
print( bool(1.46) )
a = 7
b = 9
# always last variable's value will be the answer if there
# is no 0,  otherwise 0 answer
print( a and b )
print( b and a )
a = 7
b = 6


# always first variable's value will be the answer if there
# is no 0,  otherwise 2nd variable's value


print( a or b )
print( b or a )
print( True + False )


# 7- Bitwise Operator
# & , |

a = 23
b = 48
print( a & b )    # 16
a = 14
b = 11
print( a & b )   # 10
a = 27
b = 46
print( a & b )   # 10
print( a | b )   # 63

# XOR   ^
# if both inputs are same the result is FALSE/0
# otherwise TRUE/1

a = 7         # 111
b = 5         # 101

# 010

print( a^b )


# RIGHT SHIFT OPERATOR   >>
# LEFT SHIF OPERATOR     <<


a = 19
print( a>>1 )
print( a>>2 )
print( a>>3 )
a = 23
print(a>>2)
a = 15
print( a>>2 )
a = 9
print( a<<1 )
print( a<<2 )
a = 4
print( a<<1 )
print( a<<2 )
print( a<<3 )
