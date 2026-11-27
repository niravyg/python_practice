# Take a list of numbers from the user 
list1 = list(map(int,input("Enter the elements of the list separated by the space:").split()))
# Find the second largest number in the list without using the sort or soted function 
largest = list1[0]
second_largest = None

for i in range(1,len(list1)):
    if list1[i] > largest:
        second_largest = largest
        largest = list1[i]
    elif list1[i] != largest:
        if second_largest is None or list1[i] > second_largest:
            second_largest = list[i]
            
print(f"the second largest value is: {second_largest}")