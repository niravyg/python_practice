# find missing number from the list of numbers
list1 = list(input("Enter the list of numbers separated by space: ").split())
list1 = [int(i) for i in list1]

def find_missing_value(list1):
    # for loop for accesing the each element of the list
    for i in range(len(list1)):
        # 