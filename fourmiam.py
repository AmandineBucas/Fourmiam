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
G=nx.Graph()
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
			G.add_edge(tenant,aboutissant,phero=0)			
            
        # Si le tenant et l'aboutissant ne sont pas vides :
		if tenant != '' and aboutissant == "Impasse":
			print (tenant + aboutissant)
            # Création d'un noeud entre le tenant et l'aboutissant.
			G.add_edge(tenant,commune,phero=0)

# Initialisation du graph
nx.draw_circular(G)

# Affichage du graph
plt.show()

# Initialisation de variables de départ et de fin , d'une fourmi.
CONS_DEBUT = "Rue des Iris"
CONS_FIN = "Route de Châtillon"

fourmi = creationFourmi(creation)

# Création d'une fourmi avec son nom, sa rue de début et sa rue de fin.
def creationFourmi(i):
    fourmi["nom"] = nom
    fourmi["début"] = CONST_START
    fourmi["fin"] = CONST_END

    return fourmi

# Départ de la fourmi.
fourmi = marche(G, streetIndexTab, fourmi)

# La fourmi commence à marcher 
def marche(graph, ant):

    # Initialisation du départ de la fin du graphe.
    debut = fourmi['debut']
    fin = fourmi['fin']

    #Initialisation d'une rue de départ
    premiereRue = "Place de la Liberté"

    # La fourmi marche jusqu'à ce qu'elle atteind sa destination.
    while(fin != premiereRue):
            # Choix aléatoire d'un noeud à utiliser.
            if(random.randint(0,1) == 1):
            node = graph.edges()[index][0]
        else:
            node = graph.edges()[index][1]:
        
    # Si la fourmi est de nouveau à sa rue de départ.
    if(fin == premiereRue):
        
        # Afficher la fourmi.
        return fourmi
