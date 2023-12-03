# Créé par nico, le 03/12/2023 en Python 3.7
import re

def repare(text):
    fichier=open(text, "r")
    lignes=fichier.readlines()
    chaine=""
    somme=0
    for l in range(len(lignes)):
        for k in range(len(lignes[l])):

            if lignes[l][k].isdigit():
                chaine+=lignes[l][k]

                if l!=0:
                    if not (lignes[l-1][k+1].isalpha() or lignes[l-1][k+1].isdigit() or lignes[l-1][k+1].isspace()):
                        if lignes[l-1][k+1]!='.':
                            chaine+="T"
                    if not (lignes[l-1][k].isalpha() or lignes[l-1][k].isdigit() or lignes[l-1][k].isspace()):
                        if lignes[l-1][k]!='.':
                            chaine+="T"
                    if not (lignes[l-1][k-1].isalpha() or lignes[l-1][k-1].isdigit() or lignes[l-1][k-1].isspace()):
                        if lignes[l-1][k-1]!='.':
                            chaine+="T"

                if l!=len(lignes)-1:
                    if not (lignes[l+1][k+1].isalpha() or lignes[l+1][k+1].isdigit() or lignes[l+1][k+1].isspace()):
                        if lignes[l+1][k+1]!='.':
                            chaine+="T"
                    if not (lignes[l+1][k].isalpha() or lignes[l+1][k].isdigit() or lignes[l+1][k].isspace()):
                        if lignes[l+1][k]!='.':
                            chaine+="T"
                    if not (lignes[l+1][k-1].isalpha() or lignes[l+1][k-1].isdigit() or lignes[l+1][k-1].isspace()):
                        if lignes[l+1][k-1]!='.':
                            chaine+="T"



                if not (lignes[l][k+1].isalpha() or lignes[l][k+1].isdigit() or lignes[l][k+1].isspace()):
                    if lignes[l][k+1]!='.':
                        chaine+="T"
                if not (lignes[l][k-1].isalpha() or lignes[l][k-1].isdigit() or lignes[l][k-1].isspace()):
                    if lignes[l][k-1]!='.':
                        chaine+="T"
            else:
                chaine+="."
    fin=chaine.split(".")
    fin=list(filter(None,fin))
    for t in range(len(fin)):
        if "T" not in fin[t]:
            fin[t]=""
    fin=list(filter(None,fin))
    for t in range(len(fin)):
        fin[t] = re.sub("T","",fin[t])
    for i in fin:
        somme+=int(i)
    print("La somme totale est : ", somme)


repare("ficj3.txt")