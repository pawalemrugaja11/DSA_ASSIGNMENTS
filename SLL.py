class node:
    def __init__(self, value):
        self.data = value
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = new_node

    def insert(self, value, pos):
        new_node = node(value)

        if pos == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            i = 1

            while(i < pos - 1 and temp != None):
                temp = temp.next
                i = i + 1

            if temp == None:
                print("Invalid position")
            else:
                new_node.next = temp.next
                temp.next = new_node

    def delete_alternate(self):
        temp = self.head

        while(temp and temp.next):
            temp.next = temp.next.next
            temp = temp.next

    def traverse(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


list1 = SLL()

list1.append(node(10))
list1.append(node(20))
list1.append(node(30))
list1.append(node(40))
list1.append(node(50))

print("Original list:")
list1.traverse()

list1.insert(15, 2)

print("After insertion:")
list1.traverse()

list1.delete_alternate()

print("After deleting alternate nodes:")
list1.traverse()
