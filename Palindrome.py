# check whether the given string is palindrome or not
var1 = input("Enter the string to check for palindrome:")
var2 = var1.replace(" ", "").lower()
if var2 == var2[::-1]:
    print(f"The string '{var1}' is a palindrome.")
else:
    print(f"The string '{var1}' is not a palindrome.")
    
