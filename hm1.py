class Node:
    """Клас вузла однозв'язного списку"""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Клас однозв'язного списку"""
    def __init__(self):
        self.head = None

    def append(self, data):
        """Додає елемент у кінець списку"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        """Виводить елементи списку"""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        """Реверсування списку, змінюючи посилання між вузлами"""
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def merge_sort(self):
        """Сортування списку злиттям"""
        def split(head):
            slow = head
            fast = head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            middle = slow.next
            slow.next = None
            return head, middle

        def merge(left, right):
            dummy = Node(0)
            tail = dummy
            while left and right:
                if left.data < right.data:
                    tail.next = left
                    left = left.next
                else:
                    tail.next = right
                    right = right.next
                tail = tail.next
            tail.next = left or right
            return dummy.next

        def merge_sort_rec(head):
            if not head or not head.next:
                return head
            left, right = split(head)
            left = merge_sort_rec(left)
            right = merge_sort_rec(right)
            return merge(left, right)

        self.head = merge_sort_rec(self.head)

    @staticmethod
    def merge_sorted_lists(l1, l2):
        """Об'єднання двох відсортованих списків"""
        dummy = Node(0)
        tail = dummy
        while l1 and l2:
            if l1.data < l2.data:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 or l2
        result = LinkedList()
        result.head = dummy.next
        return result

#створення списку
print("Оригінальний список:")
ll = LinkedList()
for value in [7, 3, 9, 1, 5]:
    ll.append(value)
ll.print_list()

#реверсування
print("Після реверсування:")
ll.reverse()
ll.print_list()

#сортування
print("Після сортування злиттям:")
ll.merge_sort()
ll.print_list()

#створення двох відсортованих списків
l1 = LinkedList()
for val in [1, 4, 7]:
    l1.append(val)

l2 = LinkedList()
for val in [2, 3, 6]:
    l2.append(val)

print("Об’єднання двох відсортованих списків:")
merged = LinkedList.merge_sorted_lists(l1.head, l2.head)
merged.print_list()
