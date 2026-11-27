
list1 = list(map(int, input("Enter the list of numbers: ").split()))

target = int(input("Enter the target sum: "))

for i in range(len(list1)):

    for j in range(i + 1, len(list1)):

        if list1[i] + list1[j] == target:

            print("Indexes:", i, j)
            print("Numbers:", list1[i], list1[j])
