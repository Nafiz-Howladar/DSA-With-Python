#stack using class

class stack:
    def __init__(self):
        self.stack  = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)

 

#Creating class
stackOne = stack()

stackOne.push("A")
stackOne.push("B")
stackOne.push("C")
stackOne.push("D")


# conducting operation
print("Stack: ", stackOne.stack)
print("Pop: ", stackOne.pop())
print("Stack after pop: ", stackOne.stack)
print("Peek: ", stackOne.peek())
print("Is empty: ", stackOne.isEmpty())
print("Size: ", stackOne.size())