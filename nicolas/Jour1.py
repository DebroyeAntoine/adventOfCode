# Créé par nico, le 01/12/2023 en Python 3.7

def somme(text):
    fichier=open(text, "r")
    lignes=fichier.readlines()
    tab=[]
    nb=[]
    somme=0
    v=-1
    for k in lignes:
        v+=1
        tab=k
        for i in tab:
            if 48<=ord(i)<=57:
                nb.append(i)
        nbDeLaLigne=nb[0]+nb[-1]
        #print(nbDeLaLigne)
        somme+=int(nbDeLaLigne)
        nbDeLaLigne=0
        nb=[]
        tab=[]
    print("La somme totale est : "+ str(somme))

def somme2(text):
    fichier=open(text, "r")
    lignes=fichier.readlines()
    nb=""
    somme=0
    for k in lignes:
        unp=k.find("one")
        up=k.find("1")
        und=k.rfind("one")
        ud=k.rfind("1")
        dep=k.find("two")
        dp=k.find("2")
        ded=k.rfind("two")
        dd=k.rfind("2")
        trp=k.find("three")
        tp=k.find("3")
        trd=k.rfind("three")
        td=k.rfind("3")
        qup=k.find("four")
        qp=k.find("4")
        qud=k.rfind("four")
        qd=k.rfind("4")
        cip=k.find("five")
        cp=k.find("5")
        cid=k.rfind("five")
        cd=k.rfind("5")
        sip=k.find("six")
        sp=k.find("6")
        sid=k.rfind("six")
        sd=k.rfind("6")
        sep=k.find("seven")
        ssp=k.find("7")
        sed=k.rfind("seven")
        ssd=k.rfind("7")
        hup=k.find("eight")
        hp=k.find("8")
        hud=k.rfind("eight")
        hd=k.rfind("8")
        nep=k.find("nine")
        np=k.find("9")
        ned=k.rfind("nine")
        nd=k.rfind("9")
        tabmaxi=[und,ded,trd,qud,cid,sid,sed,hud,ned,ud,dd,td,qd,cd,sd,ssd,hd,nd]
        maxi=-2
        indma=0
        for p in range(len(tabmaxi)):
            if tabmaxi[p]!=(-1):
                if tabmaxi[p]>=maxi:
                    maxi=tabmaxi[p]
                    indma=p
        if indma>=9:
            indma=indma-9
        tabmini=[unp,dep,trp,qup,cip,sip,sep,hup,nep,up,dp,tp,qp,cp,sp,ssp,hp,np]
        mini=1000
        indmi=0
        for p in range(len(tabmini)):

            if tabmini[p]!=(-1):
                if tabmini[p]<=mini:
                    mini=tabmini[p]
                    indmi=p
        if indmi>=9:
            indmi=indmi-9
        nb=str(indmi+1)+str(indma+1)
        somme+=int(nb)
        #print(nb)
    print("La somme totale est : "+ str(somme))

somme("ficj1.txt")
somme2("ficj1.txt")