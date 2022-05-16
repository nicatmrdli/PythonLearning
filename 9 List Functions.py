lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Karen", "Jim", "Oscar", "Toby"]

friends.extend(lucky_numbers)
# This will include lucky numbers into the friends list e.g "["Kevin, Karen, etc.. 4, 8, 15...]"

friends.append("Nicat")
# This will append (or add) additional value that you included next to the code. In this case it will add "Nicat".

friends.insert(2, "Kelly")
# This will INSERT a new value next to the desired index position, in this case it added Kelly next to Karen.

friends.remove("Jim")
# This will remove any wanted value that from the set.

friends.clear()
# This will clear the entire list.

friends.pop()
# This will remove the last value from the list

friends.sort()
# This will sort number values and string value in alphabetical/numerical order.

lucky_numbers.reverse()
# This will reverse the order of the list

friends2 = friends.copy()
print(friends)
# This will copy the list and store it in different name storage

print(friends.index("Kevin"))
# This will give the index of the value. You can use this to see if a value is in the list.

print(friends.count("Karen"))
# This will show how many times the value shows up in the string