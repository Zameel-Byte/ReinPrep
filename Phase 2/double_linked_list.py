class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.prev = None


class DLinkedList:
    def add_element(self, head, value):
        new_node = Node(value)
        temp = head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
        new_node.next = None

    def add_at_start(self, head, value):
        pass

    def insert_at_pos(self, head, value, pos):
        pass

    def remove_element(self, head):
        temp = head
        while temp.next.next is not None:
            temp = temp.next
        temp.next.prev = None
        temp.next = None

    def list_print(self, head):
        temp = head
        while temp is not None:
            print(f"{temp.data}<->", end='')
            temp = temp.next
        print()

    def list_print_rev(self, head):
        temp = head
        while temp.next is not None:
            temp = temp.next
        while temp:
            print(f"<->{temp.data}", end="")
            temp = temp.prev
        print()

    def search_element(self, head, value):
        pass
    def list_rev(self, head):
        pass

    def half_rev(self, head, k):
        pass


obj = DLinkedList()
head = Node(10)
obj.add_element(head, 20)
obj.add_element(head, 30)
obj.list_print(head)
obj.list_print_rev(head)
