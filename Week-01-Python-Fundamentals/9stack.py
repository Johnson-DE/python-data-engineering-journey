#TACK PROBLEM 1 — Basic Push
"""
stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print(stack)"""

#STACK PROBLEM 2 — Pop One Item
"""stack = []

stack.append(10)
stack.append(20)
stack.append(30)

removed = stack.pop()

print(removed)
print(stack)"""
#STACK PROBLEM 3 — Peek Top Item

"""stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print(stack[-1])"""

# STACK PROBLEM 4 — Check Empty Stack

"""stack = []

if len(stack) == 0:
    print("Stack is Empty")
else:
    print("Stack has a item")
"""
#STACK PROBLEM 5 — Reverse String (Important)

name = "JOHNSON"
stack = []

for char in name:
    stack.append(char)

reversed_word = ""

while len(stack)>0 :
    reversed_word += stack.pop()

print(reversed_word)