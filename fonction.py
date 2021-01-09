import pandas, random

def affiche(tableau): #affiche le tableau
	print("\n")
	print(tableau[0],tableau[1],tableau[2])
	print(tableau[3],tableau[4],tableau[5])
	print(tableau[6],tableau[7],tableau[8])

def rank(inpu):
	ffiinn=[]
	indices = list(range(len(inpu)))
	indices.sort(key=lambda x: inpu[x])
	output = [0] * len(indices)
	for i, x in enumerate(indices):
		output[x] = i
	i=8
	while i!=-1:
		if inpu[output.index(i)]>50 and max(inpu)!=100:
			ffiinn.append(output.index(i))
		elif inpu[output.index(i)]==100:
			ffiinn.append(output.index(i))
		i=i-1
	if len(ffiinn)==0:
		ffiinn.append(output.index(8))
		ffiinn.append(output.index(7))
	qwsa=ffiinn[random.randint(0,len(ffiinn)-1)]
	#print(inpu,output)
	return [inpu[qwsa],qwsa]

def Scherche(tableaux,base,tableau):
	cherche=int("".join(tableaux))
	G=[]
	P=[]
	N=[]
	i=1
	chercheN=cherche*10
	while i!=10:
		chercheN=chercheN+1
		i=i+1
		resultat=base[base['etape'] == chercheN]
		if len(resultat)!=0:
			resultatG=base[base['etape'] == chercheN][base['G-P'] == 'P']
			G.append(int((len(resultatG)*100)/len(resultat)))
			resultatN=base[base['etape'] == chercheN][base['G-P'] == 'N']
			N.append(int((len(resultatN)*100)/len(resultat)))
		else:
			G.append(0)
			P.append(0)
			N.append(0)
	
	PG=rank(G)
	PN=rank(N)

	if PG[0] == PN[0] == 0:
		deja=0
		joue,deja=dejagagne("O",deja,tableau)
		if deja == 0:
			joue,deja=dejagagne("X",deja,tableau)
		if deja == 0:
			joue=random.randint(0, 8)
			while tableau[joue] != "-":
				joue=random.randint(0, 8)
		return joue+1
	else:
		if PG[0]>PN[0]:
			return PG[1]+1
		else:
			return PN[1]+1

def gagnant(tableau,tour,fin,score):
	if (tableau[0] == tableau[1] == tableau[2] != "-") and fin != 1:
		#dit le gagnant
		if tableau[0] == "X" :
			print("\n\n")
			affiche(tableau)
			print("\n")
			print("Bravo, vous avez gagné")
			score[0]=score[0]+1
			return 1,score
		else :
			print("\n\n")
			affiche(tableau)
			print("\n")
			print("Dommage, vous avez perdu")
			score[1]=score[1]+1
			return 1,score
	elif (tableau[3] == tableau[4] == tableau[5] != "-") and fin != 1:
		#dit le gagnant
		if tableau[3] == "X" :
			print("\n\n")
			affiche(tableau)
			print("\n")
			print("Bravo, vous avez gagné")
			score[0]=score[0]+1
			return 1,score
		else :
			print("\n\n")
			affiche(tableau)
			print("\n")
			print("Dommage, vous avez perdu")
			score[1]=score[1]+1
			return 1,score
	elif (tableau[6] == tableau[7] == tableau[8] != "-") and fin != 1:
		#dit le gagnant
		if tableau[6] == "X" :
			print("\n\n")
			affiche(tableau)
			print("\n")
			print("Bravo, vous avez gagné")
			score[0]=score[0]+1
			return 1,score
		else :
			print("\n\n")
			affiche(tableau)
			print("\n")
			print("Dommage, vous avez perdu")
			score[1]=score[1]+1
			return 1,score
	elif (tableau[0] == tableau[3] == tableau[6] != "-") and fin != 1:
		#dit le gagnant
		if tableau[0] == "X" :
			print("\n\n")
			affiche(tableau)
			print("\n")
			print("Bravo, vous avez gagné")
			score[0]=score[0]+1
			return 1,score
		else :
			print("\n\n")
			affiche(tableau)
			print("\n")
			print("Dommage, vous avez perdu")
			score[1]=score[1]+1
			return 1,score
	elif (tableau[1] == tableau[4] == tableau[7] != "-") and fin != 1:
		#dit le gagnant
		if tableau[1] == "X" :
			print("\n\n")
			affiche(tableau)
			print("\n")
			print("Bravo, vous avez gagné")
			score[0]=score[0]+1
			return 1,score
		else :
			print("\n\n")
			affiche(tableau)
			print("\n")
			print("Dommage, vous avez perdu")
			score[1]=score[1]+1
			return 1,score
	elif (tableau[2] == tableau[5] == tableau[8] != "-") and fin != 1:
		#dit le gagnant
		if tableau[2] == "X" :
			print("\n\n")
			affiche(tableau)
			print("\n")
			print("Bravo, vous avez gagné")
			score[0]=score[0]+1
			return 1,score
		else :
			print("\n\n")
			affiche(tableau)
			print("\n")
			print("Dommage, vous avez perdu")
			score[1]=score[1]+1
			return 1,score
	elif (tableau[0] == tableau[4] == tableau[8] != "-") and fin != 1:
		#dit le gagnant
		if tableau[0] == "X" :
			print("\n\n")
			affiche(tableau)
			print("\n")
			print("Bravo, vous avez gagné")
			score[0]=score[0]+1
			return 1,score
		else :
			print("\n\n")
			affiche(tableau)
			print("\n")
			print("Dommage, vous avez perdu")
			score[1]=score[1]+1
			return 1,score
	elif (tableau[2] == tableau[4] == tableau[6] != "-") and fin != 1:
		#dit le gagnant
		if tableau[2] == "X" :
			print("\n\n")
			affiche(tableau)
			print("\n")
			print("Bravo, vous avez gagné")
			score[0]=score[0]+1
			return 1,score
		else :
			print("\n\n")
			affiche(tableau)
			print("\n")
			print("Dommage, vous avez perdu")
			score[1]=score[1]+1
			return 1,score
	elif (tour == 9 and fin != 1) or ("-" not in tableau):
		#dit le gagnant
		print("\n\n")
		affiche(tableau)
		print("\n")
		print("Dommage, c'est une égalité")
		return 1,score
	else:
		return 0,score

def dejagagne(x,deja,tableau):
	joue=0
	deja=0
	if (((tableau[0] == tableau[1] == x) and ("-" == tableau[2])) or ((tableau[0] == tableau[2] == x) and ("-" == tableau[1])) or ((tableau[1] == tableau[2] == x) and ("-" == tableau[0]))):
		if tableau[0] == "-":
			joue=0
			deja=1
		if tableau[1] == "-":
			joue=1
			deja=1
		if tableau[2] == "-":
			joue=2
			deja=1
	elif (((tableau[3] == tableau[4] == x) and ("-" == tableau[5])) or ((tableau[3] == tableau[5] == x) and ("-" == tableau[4])) or ((tableau[4] == tableau[5] == x) and ("-" == tableau[3]))):
		if tableau[3] == "-":
			joue=3
			deja=1
		if tableau[4] == "-":
			joue=4
			deja=1
		if tableau[5] == "-":
			joue=5
			deja=1
	elif (((tableau[6] == tableau[7] == x) and ("-" == tableau[8])) or ((tableau[6] == tableau[8] == x) and ("-" == tableau[7])) or ((tableau[7] == tableau[8] == x) and ("-" == tableau[6]))):
		if tableau[6] == "-":
			joue=6
			deja=1
		if tableau[7] == "-":
			joue=7
			deja=1
		if tableau[8] == "-":
			joue=8
			deja=1
	elif (((tableau[0] == tableau[3] == x) and ("-" == tableau[6])) or ((tableau[0] == tableau[6] == x) and ("-" == tableau[3])) or ((tableau[3] == tableau[6] == x) and ("-" == tableau[0]))):
		if tableau[0] == "-":
			joue=0
			deja=1
		if tableau[3] == "-":
			joue=3
			deja=1
		if tableau[6] == "-":
			joue=6
			deja=1
	elif (((tableau[1] == tableau[4] == x) and ("-" == tableau[7])) or ((tableau[1] == tableau[7] == x) and ("-" == tableau[4])) or ((tableau[4] == tableau[7] == x) and ("-" == tableau[1]))):
		if tableau[1] == "-":
			joue=1
			deja=1
		if tableau[4] == "-":
			joue=4
			deja=1
		if tableau[7] == "-":
			joue=7
			deja=1
	elif (((tableau[2] == tableau[5] == x) and ("-" == tableau[8])) or ((tableau[2] == tableau[8] == x) and ("-" == tableau[5])) or ((tableau[5] == tableau[8] == x) and ("-" == tableau[2]))):
		if tableau[2] == "-":
			joue=2
			deja=1
		if tableau[5] == "-":
			joue=5
			deja=1
		if tableau[8] == "-":
			joue=8
			deja=1
	elif (((tableau[0] == tableau[4] == x) and ("-" == tableau[8])) or ((tableau[0] == tableau[8] == x) and ("-" == tableau[4])) or ((tableau[4] == tableau[8] == x) and ("-" == tableau[0]))):
		if tableau[0] == "-":
			joue=0
			deja=1
		if tableau[4] == "-":
			joue=4
			deja=1
		if tableau[8] == "-":
			joue=8
			deja=1
	elif (((tableau[2] == tableau[4] == x) and ("-" == tableau[6])) or ((tableau[2] == tableau[6] == x) and ("-" == tableau[4])) or ((tableau[4] == tableau[6] == x) and ("-" == tableau[2]))):
		if tableau[2] == "-":
			joue=2
			deja=1
		if tableau[4] == "-":
			joue=4
			deja=1
		if tableau[6] == "-":
			joue=6
			deja=1
	return joue,deja