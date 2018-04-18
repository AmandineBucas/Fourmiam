# -*- coding: utf-8 -*-
"""
TP FOURMIAM - AMANDINE BUCAS : I4
Utilisation de l'ACO afin de trouver le meilleur itinéraire pour un robot de livraison.
"""

# Imports utiles pour l'algorithme (csv, fonctions de dessin etc).
import math
import csv
import networkx as nx
import matplotlib.pyplot as plt
 
# Initialisation du graphe.
# Utilisation de networkx permettant la création / manipulation des graphes.
graph=nx.Graph()
nx.draw(G)  
plt.draw()

# Import du CSV possédant les informations des diverses rues nantaises.
with open('VOIES_NM.csv', encoding='UTF8') as csvfile:
        
    # Lecture du fichier de csv.
	reader = csv.DictReader(csvfile)
	# lecture de chaque ligne du fichier csv.
	for row in reader:

        # Initialisation de la rue.
		rue = row['LIBELLE']        
        # Initialisation du tenant.
		tenant = row['TENANT']                
        # Initialisation de l'aboutissant. 
		aboutissant = row['ABOUTISSANT']        
        # Initialisation de l'aboutissant. 
		statut = row['STATUT']
        # Initialisation de l'aboutissant. 
		commune = row['COMMUNE']
        # Initialisation des points de la route.
		point = row['BI_MAX']	

        # Si le tenant et l'aboutissant ne sont pas vides :
		if tenant != '' and aboutissant != '':
			print (tenant + aboutissant)
            # Création d'un noeud entre le tenant et l'aboutissant.
			graph.add_edge(tenant,aboutissant,phero=0)			
            
        # Si le tenant et l'aboutissant ne sont pas vides :
		if tenant != '' and aboutissant == "Impasse":
			print (tenant + aboutissant)
            # Création d'un noeud entre le tenant et l'aboutissant.
			graph.add_edge(tenant,commune,phero=0)
            
            graph = pertePheromone(graph, fourmi)

# Initialisation du graph
nx.draw_circular(graph)

# Affichage du graph
plt.show()

# Initialisation de variables de départ et de fin , d'une fourmi.
CONS_DEBUT = "Rue des Iris"
CONS_FIN = "Route de Châtillon"

fourmi = creationFourmi(creation)

# Création d'une fourmi avec son nom, sa rue de début, sa rue de fin, si la rue a été visité.
def creationFourmi(i):
    fourmi["nom"] = nom
    fourmi["début"] = CONS_DEBUT
    fourmi["fin"] = CONS_FIN
    fourmi["rue visitée"] = {}
    fourmi["chemin parcouru"] = 0

    return fourmi

# Départ de la fourmi.
fourmi = marche(graph, fourmi)

# La fourmi commence à marcher 
def marche(graph, fourmi):

    # Initialisation du départ et de la fin.
    debut = fourmi['debut']
    fin = fourmi['fin']

    #Initialisation d'une rue de départ
    premiereRue = "Place de la Liberté"

    # La fourmi marche jusqu'à ce qu'elle atteind sa destination.
    while(fin != premiereRue):
            # Choix aléatoire d'un noeud à utiliser.
            if(random.randint(0,1) == 1):
            noeud = graph.edges()[index][0]
        else:
            noeud = graph.edges()[index][1]
            
            # On choisi une rue aléatoirement
            choixFourmi = choixRue(graph.edges(noeud, data='rue'))
        
    # Si la fourmi est de nouveau à sa rue de départ.
    if(fin == premiereRue):
        
        # Afficher la fourmi.
        return fourmi

# Fonction de fitness : Sur rues déjà visitées.
def pheromoneDrop(graph, fourmi):

    # Perte de phéromones lors de la marche de la fourmi.
    rue = fourmi["pertePheromone"]
    for i in rue:
        if(fourmi["chemin parcouru"] > 1):
            # Calcul des pheromones en fonction du chemin parcouru.
            pheromone =  1 / fourmi["chemin parcouru"]
            pheromone = str(pheromone)
        graph.edges(data='pheromone')['pheromone']

    return graph

