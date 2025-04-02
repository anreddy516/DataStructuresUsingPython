from ds.my_stack import MyStack

my_stack = MyStack(4)

choice = int(input("Enter your choice : "))

while(True):
    if (choice == 6):
        print("Exited")
        break

    if (choice == 1):
        item = int(input("Enter item to be pushed : "))
        my_stack.push(item)
        my_stack.print()
    elif (choice == 2):
        item = my_stack.pop()
        print(f"Got item from stack = {item}")
        my_stack.print()
    elif (choice == 3):
        item = my_stack.peek()
        print(f"Got item from stack = {item}")
        my_stack.print()
    elif (choice == 4):
        overflow = my_stack.is_stack_full()
        if (overflow):
            print("Stack is overflow")
        else:
            print("Stack is not overflow")
        my_stack.print()
    elif (choice == 5):
        underflow = my_stack.is_stack_empty()
        if (underflow):
            print("Stack is underflow")
        else:
            print("Stack is not underflow")
        my_stack.print()

    choice = int(input("Enter your choice : "))
    
        