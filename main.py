class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = new_node
            new_node.prev = curr_node

    def reverse(self):
        curr_node = self.head
        prev_node = None
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            curr_node.prev = next_node
            prev_node = curr_node
            curr_node = next_node
        self.head = prev_node

    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next



if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)

    print("До разворота:")
    linked_list.print_list()

    linked_list.reverse()

    print("После разворота:")
    linked_list.print_list()

