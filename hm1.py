class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

#функція вставки (для створення BST)
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

#функція для знаходження найбільшого значення в BST або AVL-дереві
def find_max(root):
    if root is None:
        return None  
    current = root
    while current.right is not None:
        current = current.right
    return current.key

if __name__ == "__main__":
    root = None
    values = [15, 10, 20, 8, 12, 17, 25]
    for val in values:
        root = insert(root, val)
    
    print("Найбільше значення у дереві:", find_max(root))
