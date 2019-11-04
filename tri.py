from random import*
n=int(input("nombre d'élement à tier"))
liste=[randrange(1,101) for i in range(n)]
print(liste)
for k in range (n-1,0,-1):
    m=max(liste[:k+1])
    i=liste.index(m)
    liste[k],liste[i]=liste[i],liste[k]
    print(liste)
print(liste)
