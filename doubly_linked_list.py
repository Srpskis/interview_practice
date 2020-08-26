class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self, values_list=None):
        self.head = None
        self.tail = None
        self.node_count = 0
        if values_list is not None:
            new_node = Node(values_list.pop(0))
            self.head = new_node
            self.tail = new_node
            for value in values_list:
                self.insert_at_end(value)

    def __iter__(self):
        if self.head is None:
            print("list empty")
            return
        temp = self.head
        while temp is not None:
            yield temp.value
            temp = temp.next

    def insert_at_end(self, value):
        if self.head is None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.node_count += 1
            return
        """ if we didnt have a tail: """
        # temp = self.head
        # while temp.next is not None:
        #     temp = temp.next
        # new_node = Node(value)
        # new_node.prev = temp
        # temp.next = new_node
        # self.tail = new_node
        """ because we have a tail"""
        new_node = Node(value)
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.node_count += 1

    def insert_at_beginning(self, value):
        if self.head is None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.node_count += 1
            return
        new_node = Node(value)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.node_count += 1

    def insert_after(self, target_value, value):
        if self.head is None:
            raise Exception("target value not found")
        temp = self.head
        while temp is not None:
            if temp.value == target_value:
                new_node = Node(value)
                new_node.prev = temp
                new_node.next = temp.next
                if temp.next is None:
                    """ if we have a tail """
                    self.tail = new_node
                else:
                    temp.next.prev = new_node
                temp.next = new_node
                self.node_count += 1
                return
            else:
                temp = temp.next
        if temp is None:
            raise Exception("target value not found")

    def insert_before(self, target_value, value):
        if self.head is None:
            raise Exception("target value not found")
        temp = self.head
        while temp is not None:
            if temp.value == target_value:
                new_node = Node(value)
                new_node.prev = temp.prev
                new_node.next = temp
                if temp.prev is None:
                    self.head = new_node
                else:
                    temp.prev.next = new_node
                temp.prev = new_node
                self.node_count += 1
                return
            else:
                temp = temp.next
            if temp is None:
                raise Exception("target value not found")

    def delete_at_end(self):
        if self.head is None:
            raise Exception("list empty")

        if self.head.next is None:
            self.head = None
            self.tail = None
            self.node_count -= 1
            return

        """ because we have a tail """
        # self.tail = self.tail.prev
        # self.tail.next.prev = None
        # self.tail.next = None

        """ if we dont have a tail """
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        self.tail = temp.prev
        temp.prev.next = None
        temp.prev = None
        self.node_count -= 1

    def delete_at_beginning(self):
        if self.head is None:
            raise Exception("list empty")
        if self.head.next is None:
            self.head = None
            self.tail = None
            self.node_count -= 1
            return
        self.head = self.head.next
        self.head.prev = None
        self.node_count -= 1

    def delete_by_value(self, target_value):
        if self.head is None:
            raise Exception("value not found")
        if self.head.value == target_value:
            if self.head.next is None:
                self.head = None
                self.tail = None
                self.node_count -= 1
                return
            else:
                self.head = self.head.next
                self.node_count -= 1
                return
        temp = self.head
        while temp.next is not None:
            if temp.value == target_value:
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                temp.next = None
                temp.prev = None
                self.node_count -= 1
                return
            temp = temp.next
        if temp.value == target_value:
            self.tail = temp.prev
            temp.prev.next = None
            self.node_count -= 1
        else:
            raise Exception("target value not found")

    def reverse_linked_list(self):
        if self.head is None:
            print("list empty")
            return
        if self.head.next is None:
            return
        temp1 = self.head
        temp2 = temp1.next
        temp1.next = None
        temp1.prev = temp2
        self.tail = temp1
        while temp2 is not None:
            temp2.prev = temp2.next
            temp2.next = temp1
            temp1 = temp2
            temp2 = temp2.prev
        self.head = temp1


    def traverse(self):
        if self.head is None:
            raise Exception("list empty")
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next




# # doubly_linked_list1 = DoublyLinkedList([1, 2, 3, 4, 5, 6, 7])
# # doubly_linked_list1.traverse()
#
# doubly_linked_list2 = DoublyLinkedList()
# # doubly_linked_list2.traverse()
#
# doubly_linked_list2.insert_at_end(1)
# # doubly_linked_list2.traverse()
#
# doubly_linked_list2.insert_at_end(2)
# # doubly_linked_list2.traverse()
#
# doubly_linked_list2.insert_at_end(3)
# doubly_linked_list2.traverse()
#
# print()
# print("Head: ", doubly_linked_list2.head.value)
# print("Tail: ", doubly_linked_list2.tail.value)
#
# print()
# doubly_linked_list2.insert_at_beginning(0)
# doubly_linked_list2.traverse()
# print("Head: ", doubly_linked_list2.head.value)
# print("Tail: ", doubly_linked_list2.tail.value)
#
# print()
# doubly_linked_list2.insert_after(0, 1)
# doubly_linked_list2.traverse()
# print("Head: ", doubly_linked_list2.head.value)
# print("Tail: ", doubly_linked_list2.tail.value)
#
# # print()
# doubly_linked_list3 = DoublyLinkedList()
# # doubly_linked_list3.insert_after(0, 1)
#
# print()
# doubly_linked_list2.insert_after(1, 2)
# doubly_linked_list2.traverse()
# print("Head: ", doubly_linked_list2.head.value)
# print("Tail: ", doubly_linked_list2.tail.value)
#
#
# print()
# doubly_linked_list2.insert_after(3, 4)
# doubly_linked_list2.traverse()
# print("Head: ", doubly_linked_list2.head.value)
# print("Tail: ", doubly_linked_list2.tail.value)
#
#
# print()
# doubly_linked_list2.insert_before(0, -1)
# doubly_linked_list2.traverse()
# print("Head: ", doubly_linked_list2.head.value)
# print("Tail: ", doubly_linked_list2.tail.value)
#
#
# print()
# doubly_linked_list2.insert_before(4, 3)
# doubly_linked_list2.traverse()
# print("Head: ", doubly_linked_list2.head.value)
# print("Tail: ", doubly_linked_list2.tail.value)
#
# print()
# doubly_linked_list2.delete_at_end()
# doubly_linked_list2.traverse()
# print("Head: ", doubly_linked_list2.head.value)
# print("Tail: ", doubly_linked_list2.tail.value)
#
# print()
# doubly_linked_list2.delete_at_beginning()
# doubly_linked_list2.traverse()
# print("Head: ", doubly_linked_list2.head.value)
# print("Tail: ", doubly_linked_list2.tail.value)
#
#
# print()
# doubly_linked_list2.delete_by_value(0)
# doubly_linked_list2.traverse()
# print("Head: ", doubly_linked_list2.head.value)
# print("Tail: ", doubly_linked_list2.tail.value)
#
# print()
# doubly_linked_list2.delete_by_value(2)
# doubly_linked_list2.traverse()
# print("Head: ", doubly_linked_list2.head.value)
# print("Tail: ", doubly_linked_list2.tail.value)
#
# print()
# doubly_linked_list2.delete_by_value(3)
# doubly_linked_list2.traverse()
# print("Head: ", doubly_linked_list2.head.value)
# print("Tail: ", doubly_linked_list2.tail.value)
#
# print()
# doubly_linked_list2.delete_by_value(3)
# doubly_linked_list2.traverse()
# print("Head: ", doubly_linked_list2.head.value)
# print("Tail: ", doubly_linked_list2.tail.value)
#
# print()
# for each in doubly_linked_list2:
#     print(each)
#
# for each in doubly_linked_list2:
#     if each == 1:
#         doubly_linked_list2.delete_by_value(1)
#
# print()
# doubly_linked_list2.traverse()
# print("Head: ", doubly_linked_list2.head.value)
# print("Tail: ", doubly_linked_list2.tail.value)

print()
doubly_linked_list4 = DoublyLinkedList([1, 2, 3, 4, 5])
doubly_linked_list4.traverse()
print("Head: ", doubly_linked_list4.head.value)
print("Tail: ", doubly_linked_list4.tail.value)
print()
doubly_linked_list4.reverse_linked_list()
doubly_linked_list4.traverse()
print("Head: ", doubly_linked_list4.head.value)
print("Tail: ", doubly_linked_list4.tail.value)