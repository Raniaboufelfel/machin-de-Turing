#Boufelfel Rania
def turing_M (  etatinitial = None,
                blanc = None,
                regle = [], 
                mot = [],    #le mot qui vou voulez virifier
                etatfinal = None, 
                pos = 0):
    st = etatinitial
    if not mot: mot = [blanc]
    if pos <0 : pos += len(mot)
    if pos >= len(mot) or pos < 0 : 
        print ("La position est mal initialisée")
        
    regle = dict(((s0, v0), (v1, dr, s1)) for (s0, v0, v1, dr, s1) in regle)
    #etat p(s0)	       la lattre 1(v0)	         la  lattre remplacer x(v1)         derction R(dr)	     etat suivante p(s1)
    while True:
        print (st, '\t', end=" ")
        for i, v in enumerate(mot):
            if i==pos: 
                print ("[%s]"%(v,),end=" ") #afiicher la lettre dans le mot
            else: 
                print (v, end=" ") #afiicher le reste de mot
        print()
        
        if st == etatfinal: #ki ykoun wsl l etat final ye5rj
            print("\n\n le mot appartint")
            break
        if (st, mot[pos]) not in regle: #etat w la leter makanch fl machin
            print("\n \n le mot n'appertin pas")
            break
        
        (v1,dr,s1) = regle [(st, mot[pos])]
        mot[pos]=v1 #lharf jdid
        #la plase de machine (la pozition)
        if dr == 'left':
            if pos > 0: pos -= 1
            else: 
                mot.insert(0, blanc)#yzid l blanc ll mot
        if dr == 'right':
            pos += 1
            if pos >= len(mot):
                mot.append(blanc)#yzid l blanc ll mot
        st = s1
##***********************************************************

def mots(mott):
    turing_M(etatinitial = 'q0',
            blanc = '$',
            mot = list(mott),
            etatfinal = 'q4',
            regle = map(tuple,
                        [
                        "q0 c c right q0".split(),
                        "q0 b c right q2".split(),
                        "q0 a c right q1".split(),
                        "q2 b b right q2".split(),
                        "q1 c c right q1".split(),
                        "q1 a a right q1".split(),
                        "q1 b c right q3".split(),
                        "q2 c c right q2".split(),
                        "q2 c a right q3".split(),
                        "q3 b b left q3".split(),
                        "q3 a a left q3".split(),
                        "q3 c c left q3".split(),
                        "q3 $ $ right q0".split(),
                        "q0 $ $ left q4".split(),
                        ]   
                        )
        
    )

#maine
print()
print("La machine turing qui virifier \n\t\t {a,b}* tq le nb de a = le nb de b")
z='y'
while z=='y'or z=='Y':
    a=input("\n\ndonner le mot : " )
    mots(a)
    z=input("\n\n Eenter 'Y' pour contunu \t 'N'pour Sortier :")
print()


