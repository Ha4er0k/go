from collections import deque
import networkx as nx

# Підготуємо той самий граф, що й у Завданні 1
G = nx.Graph()

lines = {
    "50": ["Isolatorweg","Sloterdijk","De Vlugtlaan","Jan van Galenstraat",
           "Postjesweg","Lelylaan","Heemstedestraat","Henk Sneevlietweg",
           "Amstelveenseweg","Zuid","RAI","Overamstel","Van der Madeweg",
           "Duivendrecht","Strandvliet","Bijlmer ArenA","Bullewijk",
           "Holendrecht","Reigersbos","Gein"],
    "51": ["Isolatorweg","Sloterdijk","Lelylaan","Heemstedestraat",
           "Henk Sneevlietweg","Amstelveenseweg","Zuid","Centraal",
           "Amstel"],
    "52": ["Noord","Noorderpark","Centraal","Rokin","Vijzelgracht",
           "De Pijp","Europaplein","Zuid"],
    "53": ["Centraal","Nieuwmarkt","Waterlooplein","Weesperplein",
           "Wibautstraat","Amstel","Spaklerweg","Van der Madeweg",
           "Venserpolder","Diemen Zuid","Verrijn Stuartweg",
           "Ganzenhoef","Kraaiennest","Gaasperplas"],
    "54": ["Centraal","Nieuwmarkt","Waterlooplein","Weesperplein",
           "Wibautstraat","Amstel","Spaklerweg","Van der Madeweg",
           "Duivendrecht","Strandvliet","Bijlmer ArenA","Bullewijk",
           "Holendrecht","Reigersbos","Gein"]
}

for stations in lines.values():
    for i in range(len(stations) - 1):
        G.add_edge(stations[i], stations[i + 1])

# Алгоритм DFS (рекурсивно)
def dfs_path(graph, start, goal, path=None, visited=None):
    if path is None:
        path = [start]
    if visited is None:
        visited = set()
    visited.add(start)

    if start == goal:
        return path

    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            result = dfs_path(graph, neighbor, goal, path + [neighbor], visited)
            if result:
                return result
    return None

# Алгоритм BFS (черга)
def bfs_path(graph, start, goal):
    visited = set()
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in graph.neighbors(node):
                new_path = path + [neighbor]
                queue.append(new_path)
    return None

# Вхідні дані
start_station = "Isolatorweg"
end_station = "Gaasperplas"

# Обчислення
dfs_result = dfs_path(G, start_station, end_station)
bfs_result = bfs_path(G, start_station, end_station)

# Результати
print("🔎 DFS шлях:")
print(" → ".join(dfs_result))
print("\n🔎 BFS шлях:")
print(" → ".join(bfs_result))
