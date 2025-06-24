import uuid
import matplotlib.pyplot as plt
import networkx as nx
from collections import deque
import matplotlib.colors as mcolors

class Node:
    def __init__(self, key, color="#1296f0"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4()) 

def build_heap_tree(heap_array, index=0):
    if index >= len(heap_array):
        return None
    node = Node(heap_array[index])
    node.left = build_heap_tree(heap_array, 2 * index + 1)
    node.right = build_heap_tree(heap_array, 2 * index + 2)
    return node

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, title=""):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    colors = [tree.nodes[n]['color'] for n in tree.nodes()]
    labels = {n: tree.nodes[n]['label'] for n in tree.nodes()}

    plt.figure(figsize=(10, 6))
    plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def get_color_gradient(n, base_color="#1296f0"):
    rgb = mcolors.hex2color(base_color)
    hsv = mcolors.rgb_to_hsv(rgb)
    colors = []
    for i in range(n):
        factor = 0.4 + 0.6 * (i / max(1, n - 1))  # від 0.4 до 1.0
        modified = mcolors.hsv_to_rgb((hsv[0], hsv[1] * factor, hsv[2] * factor))
        colors.append(mcolors.to_hex(modified))
    return colors

def dfs_traversal(root):
    stack = [root]
    visited = []
    while stack:
        node = stack.pop()
        if node:
            visited.append(node)
            stack.append(node.right)
            stack.append(node.left)
    return visited

def bfs_traversal(root):
    queue = deque([root])
    visited = []
    while queue:
        node = queue.popleft()
        if node:
            visited.append(node)
            queue.append(node.left)
            queue.append(node.right)
    return visited

if __name__ == "__main__":
    heap = [0, 4, 1, 5, 10, 3]
    root = build_heap_tree(heap)

    dfs_nodes = dfs_traversal(root)
    dfs_colors = get_color_gradient(len(dfs_nodes))
    for node, color in zip(dfs_nodes, dfs_colors):
        node.color = color
    draw_tree(root, title="DFS обхід (вглибину)")

    for node in dfs_nodes:
        node.color = "#1296f0"

    bfs_nodes = bfs_traversal(root)
    bfs_colors = get_color_gradient(len(bfs_nodes))
    for node, color in zip(bfs_nodes, bfs_colors):
        node.color = color
    draw_tree(root, title="BFS обхід (вширину)")
