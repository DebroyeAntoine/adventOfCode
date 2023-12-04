# Créé par ndebr, le 04/12/2023 en Python 3.7
def jouer(text):
    fichier=open(text, "r")
    lignes=fichier.readlines()
    somme=0
    for k in lignes:
        points=0
        chiffre=k.split(':')
        chiffre=[k for k in chiffre]
        ensemble=chiffre[1].split('|')
        gagnants=ensemble[0].split(" ")
        miens=ensemble[1].split(" ")
        gagnants=list(filter(None,gagnants))
        miens=list(filter(None,miens))
        miens[-1]=miens[-1][:-1]
        for i in range(len(gagnants)):
            if gagnants[i] in miens:
                if points==0:
                    points+=1
                else:
                    points=points*2
        somme+=points
    print("la somme totale est : ",somme)

def jouer2(text):
    fichier=open(text, "r")
    lignes=fichier.readlines()
    somme=0
    nbcartes=[1 for k in range(len(lignes))]
    for k in range(len(lignes)):
        n=0
        chiffre=lignes[k].split(':')
        chiffre=[k for k in chiffre]
        ensemble=chiffre[1].split('|')
        gagnants=ensemble[0].split(" ")
        miens=ensemble[1].split(" ")
        gagnants=list(filter(None,gagnants))
        miens=list(filter(None,miens))
        miens[-1]=miens[-1][:-1]
        for i in range(len(gagnants)):
            if gagnants[i] in miens:
                n+=1
        for l in range(k,n+k):
            for y in range(nbcartes[k]):
                nbcartes[l+1]+=1

        somme=sum(nbcartes)
    print("la somme totale est : ",somme)

jouer("ficj4.txt")
jouer2("ficj4.txt")