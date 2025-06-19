import networkx as nx

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

#додавання ребра з вагою (2 хв між сусідніми станціями)
for stations in lines.values():
    for i in range(len(stations) - 1):
        G.add_edge(stations[i], stations[i + 1], weight=2)

#Алгоритм Дейкстри - найкоротші шляхи між усіма вершинами
shortest_paths = dict(nx.all_pairs_dijkstra_path_length(G, weight='weight'))

#приклад: час від Isolatorweg до всіх станцій
print("Найкоротший час від 'Isolatorweg' до інших станцій (в хвилинах):\n")
for station, time in sorted(shortest_paths["Isolatorweg"].items(), key=lambda x: x[1]):
    print(f"{station}: {time} хв")
