class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            self._insert_helper(new_node, self.head)

    def _insert_helper(self, new_node, current):
        if current.next == self.head:
            current.next = new_node
            new_node.next = self.head
            return
        self._insert_helper(new_node, current.next)

    def display(self, current=None):
        if not current:
            current = self.head
        print(current.data, end=' ')
        if current.next != self.head:
            self.display(current.next)

    def sum_even(self, current=None):
        if not current:
            current = self.head
        if current.data % 2 == 0:
            sum = current.data
        else:
            sum = 0
        if current.next != self.head:
            return sum + self.sum_even(current.next)
        return sum

# Create the circular linked list
c_list = CircularLinkedList()
c_list.insert(1)
c_list.insert(2)
c_list.insert(3)
c_list.insert(4)
c_list.insert(5)
c_list.insert(6)

# Display the list
print('Список:')
c_list.display()

# Compute the sum of even value nodes in the list
sum_even = c_list.sum_even()
print('\nСума елементів із парними значеннями:', sum_even,sep='\n',end=' ')
