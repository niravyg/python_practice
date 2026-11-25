# Revese a string without using [::-1]

var1 = input("Enter the String to be reversed: ")
var2 = list(var1)
var2.reverse()
var3 = ''.join(var2)
print(f"The reversed string is : {var3}")