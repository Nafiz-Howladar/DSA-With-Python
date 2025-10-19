#stack in python 

stack = []

#Push in Stack
stack.append("A")
stack.append("B")
stack.append("C")
stack.append("D")
stack.append("E")
print("stack: ", stack)

#Pop in stack
popedElement = stack.pop()
print("popedElement: ", popedElement)

#Stack after pop
print("Stack after pop: ", stack)

#is empty 
isEmpty = not bool(stack)
print("isEmpty : ", isEmpty)

#size
stackSize = len(stack)
print("Size of list: ", stackSize)

#peek 
peek = stack[-1]
print("peek: ", peek)


#OutPut
# print(stack)