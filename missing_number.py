# Find missing number from an ascending list

list1 = list(map(int, input("Enter numbers separated by spaces: ").split()))

def missing_number(list1):

    missing_value_list = []

    for i in range(len(list1)-1):

        if list1[i+1] != list1[i]+1:

            missing_value = list1[i]+1

            missing_value_list.append(missing_value)

    return missing_value_list


var1 = missing_number(list1)
print(var1)