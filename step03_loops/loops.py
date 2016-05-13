friends = ["zia", "zeeshan", "hira", "inam"]

for friend in friends:
    print(friend)
    print(".")
print("End of list")


for value in range(1, 5):
    print(value)


numbers = list(range(20,29))
print(numbers)


digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

#list comprehension
squares = [value**2 for value in range(1,5)]
print(squares)


players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])  #slice from index 0 to index 3
print(players[:1])  #slice from 0
print(players[1:])  #slice from 1 index to last
print(players[-2:])  #slice the last two

for player in players[:3]:
    print(player.title())

copy = players[:]
print(copy)


immutable_tuple = (1, 7, 12)
print(immutable_tuple)