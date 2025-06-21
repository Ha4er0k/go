class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

#функція вставки (створення BST)
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root
#функція для знаходження суми всіх значень у дереві
def sum_tree(root):
    if root is None:
        return 0
    return root.key + sum_tree(root.left) + sum_tree(root.right)

if __name__ == "__main__":
    root = None
    values = [15, 10, 20, 8, 12, 17, 25]
    for val in values:
        root = insert(root, val)
    
    print("Сума всіх значень у дереві:", sum_tree(root))
