import heapq

graph = {}

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
        u, v = stations[i], stations[i + 1]
        graph.setdefault(u, {})[v] = 2
        graph.setdefault(v, {})[u] = 2

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    visited = set()
    heap = [(0, start)]

    while heap:
        current_distance, current_node = heapq.heappop(heap)

        if current_node in visited:
            continue
        visited.add(current_node)

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances

shortest_from_isolatorweg = dijkstra(graph, "Isolatorweg")

print("Найкоротші шляхи від станції 'Isolatorweg':\n")
for station, time in sorted(shortest_from_isolatorweg.items(), key=lambda x: x[1]):
    print(f"{station}: {time} хв")
