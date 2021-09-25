from stack_class import Stack


if __name__ == '__main__':
    string = input('Введите строку скобок: ')
    list_elements = []
    counter = 0
    dict_const = {")": "(", "]": "[", "}": "{"}
    stack = Stack(list_elements)
    for item in string:
        if item == "(" or item == "[" or item == "{":
            stack.push(item)
        if item == ")" or item == "]" or item == "}":
            if stack.size() > 0:
                element = stack.peek()
                if element == dict_const[item]:
                    stack.pop()
            else:
                break
        counter += 1

    if stack.isEmpty() and counter == len(string):
        print("Сбалансированно")
    else:
        print("Несбалансированно")
