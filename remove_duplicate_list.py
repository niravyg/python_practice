list1 = list(input("Enter the elements of the list separated by spaces: ").split())

# accessing the single elements of the list using a for loop
for i in range(len(list1)):
    j = i+1
    
    while j < len(list1):
        if list1[i] == list1[j]:
            del list1[j]
        else:
            j +=1
print(f"the list without duplicates is: {list1}")