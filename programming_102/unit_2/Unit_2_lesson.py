current_sum = 0
alist = []

def sum_numbers(number_passing):
    sumof = 0
    for number in number_passing:
        sumof += int(number)
    return sumof

user_input = (input("Enter a number to be summed: "))

while user_input != "done":

    alist.append(user_input)
    user_input = (input("Enter a number to be summed: "))

current_sum = sum_numbers(alist)

print(f"Your sum is: {current_sum}")
print(f"Your list contains: {alist}")

target = input("Enter a number to be removed: ")

def remove_all(numbers, target):
    blist = []
    for number in numbers:
        if number != target:
            blist.append(number)
    return blist

sum_list = remove_all(alist, target)
print(sum_list)