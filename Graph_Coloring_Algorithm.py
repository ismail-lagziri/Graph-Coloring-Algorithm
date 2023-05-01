from colour import Color
from copy import deepcopy
import networkx as nx
import matplotlib.pyplot as plt

D={}
C={}
couleur_map = ['#e5ffff']
G= nx.Graph()
C[0]= Color(rgb=(0.9, 1, 1))
Liste_Couleur = [C[0]]
n= int (input ("Entrer le nombre des sommets 'n' : "))

for iteration in range(n):
	G.add_node(iteration)
print(n)

for i in range(1,n):
	C[i] = 0

for i in range(n):
	Liste_Copiée=[]
	D[i]=[]
	print("Entrer le nombre de sommets adjacent à" , i)
	number = int (input())

	for l in range(number):
		print("Entrer les adjacents à" ,i, "de 0 à" , n-1 )
		a = int(input())
		D[i].append(a)
		G.add_edge(i,a) 
	Liste_Copiée = deepcopy(Liste_Couleur)

	if i > 0:
		for j in D[i]:
			if Liste_Copiée != []:
				if C[j] in Liste_Copiée:
					Liste_Copiée.remove(C[j])

		if Liste_Copiée != []:
			C[i] = Liste_Copiée[0]
			valuer = Liste_Copiée[0]
			couleur_map.append(str(globals()['valuer']))
		
		else:
			if i % 3 == 0: 
				C[i] = Color(rgb=((100 - 10*(i+1))/100,0,0))
				Liste_Couleur.append(C[i])
				Nouvelle_Couleur = Color(rgb=((100 - 10*i)/100,0,0))
				couleur_map.append(str(globals()['Nouvelle_Couleur']))
			elif i % 3 == 1:
				C[i] = Color(rgb=(0,(100 - 10*i)/100,0))
				Liste_Couleur.append(C[i])
				Nouvelle_Couleur = Color(rgb=(0,(100 - 10*i)/100,0))
				couleur_map.append(str(globals()['Nouvelle_Couleur']))
			else:
				C[i] = Color(rgb=(0, 0, (100 - 10*i)/100))
				Liste_Couleur.append(C[i])
				Nouvelle_Couleur = Color(rgb=(0, 0, (100 - 10*i)/100))
				couleur_map.append(str(globals()['Nouvelle_Couleur']))

print(D)					
print(C)
print(G.nodes())
print(G.edges())
print(couleur_map)
nx.draw(G, node_color=couleur_map, with_labels = True, node_size=600, width= 1.5,
	pos=nx.spring_layout(G, seed=42), 
        font_size=10, font_family='sans-serif',
        node_shape='o', alpha=0.9, linewidths=0.5, edge_color='gray',
        font_weight='bold', font_color='black', edgecolors='black')
plt.show()
