
class LinkedList:

    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for i in nodes:
                node.next = Node(data=i)
                node = node.next

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


def remove_dups(self):

    if not self.head:
        return Exception("List empty")
    dict1 = {}
    previous_node = self.head
    for node in self:
        if node.data not in dict1:
            dict1[node.data] = True
            previous_node = node
        else:
            previous_node.next = node.next



global llist
llist = LinkedList(["2", "1", "2", "4", "2", "3", "1"])
for node in llist:
    print(node)

print(" ")
remove_dups(llist)
for node in llist:
    print(node)