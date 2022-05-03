lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Karen", "Jim", "Oscar", "Toby"]
friends.extend(lucky_numbers)
friends.append("Nicat")
friends.insert(1, "Kelly")
friends.remove("Jim")
print(friends.count("Karen"))


friends = ["Kevin", "Karen", "Karen", "Jim", "Oscar", "Toby"]
friends.sort()
print(friends)


lucky_numbers = [4, 8, 15, 16, 23, 42]
lucky_numbers.sort()
print(lucky_numbers)


lucky_numbers = [4, 8, 15, 16, 23, 42]
lucky_numbers.reverse()
print(lucky_numbers)


friends = ["Kevin", "Karen", "Karen", "Jim", "Oscar", "Toby"]
friends2 = friends.copy()


friends = ["Kevin", "Karen", "Karen", "Jim", "Oscar", "Toby"]
friends.pop()
print(friends)
