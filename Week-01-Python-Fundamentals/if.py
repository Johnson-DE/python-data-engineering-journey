room1 = ["john", "mari", "perthis"]
room2 = ["venkat", "muthu"]
room3 = ["abin","jegan"]
room4 = ["abinesh", "arunachalam", "maha"]

name = input("enter a member name: ")

if name in room1:
    print("room1")
elif name in room2:
    print("room2")
elif name in room3:
    print("room3")
elif name in room4:
    print("room4")
else:
    print("i don't know")


