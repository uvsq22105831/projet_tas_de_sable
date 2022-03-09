#########################################
# groupe MIASHS TD01 groupe 2
# Maxime JOUAN
# Manon BARRERE
# Yacine RAFIL
# https://github.com/uvsq22105831/projet_tas_de_sable
#########################################
# import des librairies

import tkinter as tk
import random as rd


############################
# Définition des constantes

# hauteur du canevas
HAUTEUR = 600
# largeur du canevas
LARGEUR = 600
# taille de la grille
N = 4
# choix des couleurs
COUL_MUR = "grey"
COUL_VIDE = "white"

P=0.3


#######################
# fonctions

def init_terrain():
    """ Initilise le terrain de la manière suivante:
    * met à 0 la liste à 2D appelée terrain qui contient pour chaque case la 
    valeur 1 si il y a un mur, et 0 sinon
    * initialise la liste à 2D grille qui contient l'identifiant
    de chaque carré dessiné sur le canevas 
    """
    global grille, terrain
    # on réinitialise les variables et le canvas
    grille = []
    terrain = []
    canvas.delete()
    for i in range(N):
        terrain.append([0]*N)
        grille.append([0]*N)

    for i in range(N):
        for j in range(N):
            if rd.uniform(0, 1) < P:
                terrain[i][j] = 1
                couleur = COUL_MUR
            else:
                couleur = COUL_VIDE
            largeur = LARGEUR // N
            hauteur = HAUTEUR // N
            x0, y0 = i * largeur, j * hauteur
            x1, y1 = (i + 1) * largeur, (j + 1) * hauteur
            rectangle = canvas.create_rectangle((x0, y0), (x1, y1), fill=couleur)
            grille[i][j] = rectangle


#######################
# programme principal

# définition des widgets
racine = tk.Tk()
racine.title("Génération de terrain")
canvas = tk.Canvas(racine, width=LARGEUR, height=HAUTEUR, bg="blue")
# placement des widgets
canvas.grid(column=1, row=0)
bouton_sable =tk.Button(racine,text="génération sable",command=init_terrain)
init_terrain()
bouton_sable.grid(column=0,row=0)
# boucle principale
racine.mainloop()



