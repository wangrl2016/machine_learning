import sys

# Function to create a stack. It initializes size of stack as 0.
def create_stack():
    stack = []
    return stack

# Stack is empty when stack size is 0.
def is_empty(stack):
    return len(stack) == 0

# Function to add an item to stack. It increases size by 1.
def push(stack, item):
    stack.append(item)
    print(item, 'pushed to stack')

# Function to remove an item from stack. It decreases size by 1.
def pop(stack):
    if (is_empty(stack)):
        # return minus infinite
        return str(-sys.maxisze - 1)
    return stack.pop()

def peek(stack):
    if (is_empty(stack)):
        return str(-sys.maxsize - 1)
    return stack[len(stack) - 1]


if __name__ == '__main__':
    stack = create_stack()

    push(stack, str(10))
    push(stack, str(20))
    print(peek(stack))
    push(stack, str(30))
    print(pop(stack), 'popped from stack')
