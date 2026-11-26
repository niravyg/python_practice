var1 = input("Enter the string to count the frequency of characters: ")
list1 = list(var1)
print(list1)

for i in range(len(list1)):
    if list1[i] == "":
        continue
    count = 1
    for j in range(i+1, len(list1)):
        if list1[i] == list1[j]:
            count += 1
            list1[j]=""
    if list1[i] != "":
        print(f"{list1[i]}: {count}")