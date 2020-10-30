friends = ["K", "H", "T", "D", "K", "U"]
more_friends = ["Q", "W", "E"]

print(friends)
print(friends[0])
print(friends[-1])

print(friends[1:])  # everything after 1
print(friends[1:3])  # between 1 and 3

friends[1] = "QWE"
friends.extend(more_friends)
friends.append("L")
friends.insert(1, "P")

friends.remove("T")
# friends.clear()
friends.pop()  # get rid of last element

friends.index("Q")
friends.count("K")

friends.sort()
print(friends)
