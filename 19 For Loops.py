# For loops are used to loop through an iterable object (like a list, tuple, etc.)

#
for letter in 'Lily':
    print(letter)
    # This will spell out each letter in Lilly on terminal by looping.
    # This code basically means, python will for loop every word in the string.

#
our_list = ['Lily', 'Brad', 'Fatima', 'Zining']
for name in our_list:
    print(name)
    # You can also use any word for for looping, here i chose "name"
#
for index in range(10):
    print(index)
    # This will print every number from 1-10 not including 10.
#
for index in range(5, 10):
    print(index)
    # You can also select a custom range like shown above.

#
our_list1 = ['Lily', 'Brad', 'Fatima', 'Zining']
len(our_list)
# This code counts how many elements are in the list, in this case there are 4.
for index in range(len(our_list1)):
    print(our_list1[index])
    # This will allow the user to access each name on the list.

#
our_list2 = ['Lily', 'Brad', 'Fatima', 'Zining']

for our_list2 in range(5):
    if our_list2 == 0:
        print("First iteration")
    else:
        print("Not first")