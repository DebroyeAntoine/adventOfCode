# Créé par nico, le 02/12/2023 en Python 3.7

def jouer(text):
    fichier=open(text, "r")
    lignes=fichier.readlines()
    n=0
    somme=0
    for l in lignes:
        n+=1
        Game=True
        deux=l.split(':')
        ensemble=deux[1].split(';')
        if Game==True:
            for m in ensemble:
                numboule=[]
                boule=m.split(',')
                for k in boule:
                    separation=k.split(" ")
                    del(separation[0])
                    for t in separation:
                        numboule.append(t)
                if Game==True:
                    for p in range(1,len(numboule),2):
                        if numboule[p][0]=="r":
                            if int(numboule[p-1])>12:
                                Game=False
                        if numboule[p][0]=="g":
                            if int(numboule[p-1])>13:
                                Game=False
                        if numboule[p][0]=="b":
                            if int(numboule[p-1])>14:
                                Game=False
            if Game==True:
                somme+=n
    print("La somme totale est : ", somme)

def jouer2(text):
    fichier=open(text, "r")
    lignes=fichier.readlines()
    somme=0
    for l in lignes:
        deux=l.split(':')
        ensemble=deux[1].split(';')
        rouge=[]
        vert=[]
        bleu=[]
        for m in ensemble:
            numboule=[]
            boule=m.split(',')
            for k in boule:
                separation=k.split(" ")
                del(separation[0])
                for t in separation:
                    numboule.append(t)

            for p in range(1,len(numboule),2):
                if numboule[p][0]=="r":
                    rouge.append(int(numboule[p-1]))
                if numboule[p][0]=="g":
                    vert.append(int(numboule[p-1]))
                if numboule[p][0]=="b":
                    bleu.append(int(numboule[p-1]))
        maxrouge=max(rouge)
        maxvert=max(vert)
        maxbleu=max(bleu)
        produit=int(maxrouge)*int(maxvert)*int(maxbleu)
        somme+=produit


    print("La somme totale est : ", somme)

jouer("ficj2.txt")
jouer2("ficj2.txt")
