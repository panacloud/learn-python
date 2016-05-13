friends = ["Zeeshan", "Hira", "Inam", "Rehan", "Taha"]
print(friends)
print(friends[0])
print(friends[-1])#last element


friends[0] = "Hanif"
print(friends)

friends.append("Gulshan")
print(friends)

friends.insert(3, "Usuf")
print(friends)

del friends[3]
print(friends)

last = friends.pop()
print(friends)
print(last)

first = friends.pop(0)
print(friends)
print(first)

friends.remove("Inam")
print(friends)

friends.insert(0, "Inam")
friends.sort()
print(friends)

friends.insert(0, "Zeeshan")
print(sorted(friends))

friends.reverse() #reverse the order
print(friends)

print(len(friends))