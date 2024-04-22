data_stack = list()
data_stack.append(1)
data_stack.append(2)
data_stack.append(3)
print(data_stack.pop())
print(data_stack.pop())

list_stack = list()


def push(stack, data):
    list_stack.append(data)

def pop(stack) :
    if (len(stack) < 1) : 
        print("no data")
        return 
    result = list_stack[len(stack)-1]
    # list의 맨끝에 있는 값은 index -1
    result = list_stack[-1]
    del list_stack[len(stack)-1]
    print(result)
    return result

push(list_stack, 10)
push(list_stack, 20)
push(list_stack, 30)
pop(list_stack)
pop(list_stack)
pop(list_stack)
pop(list_stack)