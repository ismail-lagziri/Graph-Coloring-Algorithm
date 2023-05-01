from colour import Color
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

n = int(input("Enter the number of nodes 'n': "))

for i in range(n):
    G.add_node(i)

color_map = ['#e5ffff']

colors = [Color(rgb=(0.9, 1, 1))]

adj_dict = {}

for i in range(n):
    adj_dict[i] = []
    print("Enter the number of adjacent nodes to node", i)
    number = int(input())

    for j in range(number):
        print("Enter the adjacent node to node", i, "between 0 and", n-1)
        a = int(input())
        adj_dict[i].append(a)
        G.add_edge(i, a)

    adj_colors = [colors[j] for j in adj_dict[i] if j < i]

    available_colors = [c for c in colors if c not in adj_colors]

    if available_colors:
        color = available_colors[0]
    else:
        if i % 3 == 0:
            color = Color(rgb=((100 - 10*(i+1))/100,0,0))
        elif i % 3 == 1:
            color = Color(rgb=(0,(100 - 10*i)/100,0))
        else:
            color = Color(rgb=(0, 0, (100 - 10*i)/100))
        colors.append(color)

    color_map.append(str(color))

print(adj_dict)
print(colors)
print(G.nodes())
print(G.edges())
print(color_map)

nx.draw(G, node_color=color_map[1:], with_labels=True, node_size=600, width=1.5, 
        pos=nx.spring_layout(G, seed=42), 
        font_size=10, font_family='sans-serif',
        node_shape='o', alpha=0.9, linewidths=0.5, edge_color='gray',
        font_weight='bold', font_color='black', edgecolors='black')

plt.show()
