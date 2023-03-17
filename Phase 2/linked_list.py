class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    @staticmethod
    def add_element(head, value):
        new_node = Node(value)
        temp = head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    @staticmethod
    def add_at_start(head, value):
        new_node = Node(value)
        new_node.next = head
        head = new_node
        return head

    @staticmethod
    def insert_at_pos(head, value, pos):
        new_node = Node(value)
        curr = head
        prev = None
        while pos != 0:
            prev = curr
            curr = curr.next
            pos = pos - 1
        prev.next = new_node
        new_node.next = curr

    @staticmethod
    def remove_element(head):
        temp = head
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None

    @staticmethod
    def list_print(head):
        temp = head
        while temp is not None:
            print(f"{temp.data}->", end='')
            temp = temp.next
        print()

    @staticmethod
    def search_element(head, value):
        temp = head
        count = 0
        pos = 0
        while temp.next is not None:
            temp = temp.next
            pos += 1
            if temp.data == value:
                count += 1
                break
            else:
                count = 0
        if count != 0:
            return f"Element found at {pos}"
        else:
            return "Not Found"

    @staticmethod
    def list_rev(head):
        curr = head
        prev = None
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        head = prev
        return head

    @staticmethod
    def half_rev(head, k):
        first = head
        curr = head
        prev = None
        while k != 0:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            k -= 1
        first.next = curr
        return prev
