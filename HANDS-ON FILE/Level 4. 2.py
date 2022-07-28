class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, head):
        self.head = head

    def add_node(self, data):
        current_node = self.head

        while current_node is not None:
            if current_node.next is None:
                new_node = Node(data)
                current_node.next = new_node
                break
            current_node = current_node.next

        return new_node

    def print_nodes(self):
        current_node = self.head

        while current_node:
            print(current_node.data, end=' ')

            current_node = current_node.next

        print()

    def sum_of_nodes(self, node, n):
        nodes = []
        current_node = node

        while current_node:
            nodes.append(current_node.data)

            current_node = current_node.next

        nodes = nodes[0-n:]
        print(nodes)

        return sum(nodes)


head = Node(5)
llist = LinkedList(head)
llist.add_node(10)
llist.add_node(6)
llist.add_node(4)
llist.add_node(1)
llist.add_node(12)
llist.print_nodes()
print(llist.sum_of_nodes(head, 3))