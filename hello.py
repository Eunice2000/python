print("hello world")
if 5>13:
    print("hello")
else:
    print("eror")

"""
i am joking and learning

"""
x = float(35)
y = int(89)
z = str("eunice")
print(x*y,z)
print(type(x))
print(type(z))
p, s, d = "eunice", 12, 3.0  #Many Values to Multiple Variables

print(type(d))

#One Value to Multiple Variables
p = s = "eunice"
print(p)
print(s)
print(type(p))
print(type(s))

#Unpack a Collection
fruits = ["banaba", "orange", "pawpaw"]
x, y, z = fruits
print(x, y, z)

x = "this is python"
print(x)

x = "python"
y = "is a "
z = "programing"
print(x, y, z)

x = 245
y = 89

if x > y:
    print("you are right the answer is:" , (x+y))
else:
    print("youre wrong")

#Global Variables
p = "my name"

def myfunc():
    print(p + " is eunice")
myfunc()

#Create a variable inside a function, with the same name as the global variable

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

_kim = "i am here"

def myfunc():
   _kim = "i am outsie" 
   print("testing my this"+ _kim)

myfunc()
print("just checking" + _kim)
#If you use the global keyword, the variable belongs to the global scope:

_ayo = "he is a boy" 

def myfunc():
  global _ayo
  _ayo = "he is a girl"
#   print("i am using", _ayo)

myfunc()
print("i am using", _ayo)
