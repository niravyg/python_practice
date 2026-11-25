# largest number in a list

list1 = list(input("Enter the list to find largest number from the list:"))

for i in range(len(list1)):
    list1[i] = int(list1[i])
    
largest = list1[0]
for j in range(1,len(list1)):
    if list1[j]>largest:
        largest = list1[j]
            
print("The largest number in the list is:", largest)