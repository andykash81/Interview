
class Stack:
    def __init__(self, list_object):
        self.list_object = list_object

    def isEmpty(self):
        if len(self.list_object) == 0:
            return True
        else:
            return False

    def push(self, new_element):
        self.list_object.insert(0, new_element)

    def pop(self):
        element = self.list_object.pop(0)
        return element

    def peek(self):
        return self.list_object[0]

    def size(self):
        return len(self.list_object)
