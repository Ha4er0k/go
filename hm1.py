import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# Метро Амстердаму
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

#додавання ребер між послідовними станціями кожної лінії
for stations in lines.values():
    for i in range(len(stations) - 1):
        G.add_edge(stations[i], stations[i + 1])

#візуалізація графа
plt.figure(figsize=(16, 10))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray',
        node_size=400, font_size=8)
plt.title("Мережа метро Амстердама (реальні станції)", fontsize=14)
plt.show()
#метрики
print("Кількість станцій:", G.number_of_nodes())
print("Кількість з'єднань:", G.number_of_edges())

#ступені вершин
print("\nТоп-10 найважливіших станцій за ступенем:")
for station, degree in sorted(G.degree(), key=lambda x: x[1], reverse=True)[:10]:
    print(f"{station}: {degree}")
