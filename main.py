import pandas, random
from fonction import *

#ouvre notre base de parti
base = pandas.read_csv("monFichier_Final-test.csv", delimiter=";", keep_default_na=False)

#défini le score à 0:0
score=[0,0]

#si la personne veut continuer à jouer ou pas
Scontinuer=["non","Non","n","N","no","No"]
#on définit que oui -> première partie
continuer="oui"

while continuer not in Scontinuer: #regarde si la personne veut jouer
	#créer les tableaux
	tableau=["-"]*9 #tableau affiché
	tableaux=["0"]	#liste des endroits joué, dans l'ordre
	fintableau=[]

	#défini variable
	fin=0
	tour=0
	touran=0
	joue=0
	cherche=0
	trouver=0
	ffiinn=[]

	while fin != 1: #démare une partie
		#pose le "pion"
		touran=tour #regarde c'est le tour combien
		if tour%2==0: #si le nombre de tour joué est paire -> X de jouer -> le joeur
			affiche(tableau) #affiche le tableau
			joue=int(input("Ou ?\n"))	#demande où il veut jouer
			if tableau[joue-1] == "-":	#si l'endroit où il veut jouer est libre, il joue dedans
				tableau[joue-1]="X"
			else: #si l'endroit où il veut jouer n'est pas libre, il recommence
				tour=tour-1
		else: #si le nombre de tour joué est impaire -> O de jouer -> l'ordi
			if tableau[joue-1] == "-": #si l'endroit où il veut jouer est libre, il joue dedans -> normalement c'est le cas, mais au cas où
				tableau[joue-1]="O"
			else: #si l'endroit où il veut jouer n'est pas libre, il recommence
				tour=tour-1
		
		if touran == tour: #si tout le monde a joué au bon endroit on le met dans la liste des endroits joué
			tableaux.append(str(joue))
		tour=tour+1 #on passe au tour suivant
			
		if touran != tour and tour != 9: #si 
			#cherche
			joue=Scherche(tableaux,base,tableau)

		#quelqu'un gagne ?
		fin,score=gagnant(tableau,tour,fin,score)
		
	#affiche le score et demande s'il veut continuer	
	print("vous avez gagné",score[0],"partis et perdu",score[1],"parti.")
	continuer=input(str("Voulez-vous continuer ? \n"))