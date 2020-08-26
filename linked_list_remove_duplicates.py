
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


def kth_to_last1(self, kth):

    dict = {}
    count = 0
    node = self.head
    while node is not None:
        dict[count] = node.data
        count += 1
        node = node.next
    index = len(dict) - 1 - kth
    if index >= 0:
        print(dict[index])
    else:
        print("Out of bounds!")
        return


def kth_to_last2(self, kth):
    p1 = self.head
    p2 = self.head

    for i in range(0, kth + 1):
        if p1 is None:
            print("Out of bounds")
            return
        p1 = p1.next

    while p1 is not None:
        p1 = p1.next
        p2 = p2.next

    print(p2.data)


def delete_middle_node(n):

    if n is None and n.next is None:
        return False
    data = n.next.data
    n.data = data
    n.next = n.next.next


def partition(self, p):

    if self.head is None:
        raise Exception("list empty")

    current = self.head
    previous = self.head

    newList = LinkedList()
    temp = newList.head

    while current is not None:
        if int(current.data) < p:
            previous = current
            current = current.next
        else:
            if newList.head is None:
                newList.head = current
                temp = newList.head
                current = current.next
                previous.next = current
            else:
                temp.next = current
                temp = temp.next
                current = current.next
                previous.next = current

    temp.next = None
    previous.next = newList.head


def sum_lists1(ll1, ll2):
    stack1 = []
    stack2 = []

    str1 = ""
    str2 = ""

    node1 = ll1.head
    node2 = ll2.head

    while node1 is not None:
        stack1.append(node1.data)
        node1 = node1.next

    while node2 is not None:
        stack2.append(node2.data)
        node2 = node2.next

    for i in range(0, len(stack1)):
        x = stack1.pop()
        str1 += x

    for i in range(0, len(stack2)):
        x = stack2.pop()
        str2 += x

    sum = int(str1) + int(str2)
    strSum = str(sum)
    sumList = list(strSum)

    stack3 =[]
    for each in sumList:
        stack3.append(str(each))

    nodes = []
    for i in range(0, len(stack3)):
        x = stack3.pop()
        nodes.append(x)

    newList = LinkedList(nodes)
    for node in newList:
        print(node)


def sum_lists2(ll1, ll2):

    list1 = []
    list2 = []

    node1 = ll1.head
    node2 = ll2.head

    while node1 is not None:
        list1.append(node1.data)
        node1 = node1.next

    while node2 is not None:
        list2.append(node2.data)
        node2 = node2.next

    str1 = ""
    str2 = ""
    for each in list1:
        str1 += each

    for each in list2:
        str2 += each

    sum = int(str1) + int(str2)
    strSum = str(sum)
    sumList = list(strSum)

    newList = LinkedList(sumList)
    for node in newList:
        print(node)


def palindrome(llist):

    if llist.head is None:
        raise Exception("list empty")

    node = llist.head
    stack = []
    while node is not None:
        stack.append(node.data)
        node = node.next

    node = llist.head

    while node is not None:
        x = stack.pop()
        y = node.data
        if x == y:
            node = node.next
        else:
            return False

    return True


# Assuming list1 is always longer than list2
def intersection(ll1, ll2):

    count1 = 0
    count2 = 0

    node1 = ll1.head
    node2 = ll2.head

    while node1 is not None:
        count1 += 1
        node1 = node1.next

    while node2 is not None:
        count2 += 1
        node2 = node2.next

    offset = count1 - count2
    if offset > 0:
        node1 = ll1.head
        node2 = ll2.head
        for i in range(0, offset):
            node1 = node1.next

        while node1 != node2:
            node1 = node1.next
            node2 = node2.next

        return node1.data


def loop_detection(llist):

    if llist.head is None:
        raise Exception("list empty")

    node = llist.head
    dict ={}

    while node not in dict:
        dict[node] = node.data
        node = node.next

    return node.data




# global llist
# llist = LinkedList(["2", "1", "2", "4", "2", "3", "1"])
# llist2 = LinkedList(["a","b","c", "d", "e", "f"])


# n = llist2.head.next.next.next



# for node in llist:
#     print(node)

# print(".................................")
# print(" ")
# remove_dups(llist)
# for node in llist:
#     print(node)

# kth_to_last1(llist, 2)
# kth_to_last2(llist, 2)

# delete_middle_node(n)
# for node in llist2:
#     print(node)

# llist3 = LinkedList(["3", "5", "8", "5", "10", "2", "1"])
# p = 5
# for node in llist3:
#     print(node)
# print(".................................")
# partition(llist3, 5)
# for node in llist3:
#     print(node)


# llist1 = LinkedList(["7", "1", "6"])
# llist2 = LinkedList(["5", "9", "2"])
# # sum_lists1(llist1, llist2)
# sum_lists2(llist1, llist2)


# llist = LinkedList(["m", "a", "d", "a", "m"])
# llist2 = LinkedList(["n","o","t"])
# print(palindrome(llist2))

llist1 = LinkedList(["3", "1", "5", "9", "7", "2", "1"])
llist2 = LinkedList(["4", "6"])


# INTERSECTION
# node1 = llist1.head
# node2 = llist2.head
# for i in range(0, 4):
#     node1 = node1.next
#
# while node2.next is not None:
#     node2 = node2.next
# node2.next = node1
#
# for node in llist1:
#     print(node)
#
# print("...................")
# for node in llist2:
#     print(node)
# print("...................")
#
# print(intersection(llist1, llist2))

# LOOP DETECTION
llist = LinkedList(["A","B","C","D","E"])
node = llist.head

temp = llist.head
while temp.next is not None:
    temp = temp.next
temp.next = node.next.next

print(loop_detection(llist))