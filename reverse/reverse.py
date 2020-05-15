class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        prev = None
        current = self.head 
        while(current is not None): 
            next = current.next_node
            current.next_node = prev 
            prev = current 
            current = next
        self.head = prev 

    def print_list(self):
        current = self.head
        self.temp = []
        while current:
            self.temp.append(current.get_value())
            current = current.next_node
        print(self.temp) 

if __name__ == '__main__':
    sll = LinkedList()
    sll.add_to_head(1)
    sll.add_to_head(2)
    sll.add_to_head(3)
    sll.add_to_head(4)
    sll.add_to_head(5)
    sll.print_list()
    sll.reverse_list(sll.head, None)
    sll.print_list()
