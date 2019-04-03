from random import*
n=int(input("nombre d'élement à tier"))
liste=[randrange(1,101) for i in range(n)]
print(liste)
for k in range (0,n-1,+1) :
    for k in range (0,n-1,+1):
        if liste[k]>liste[k+1]:
            liste[k],liste[k+1]=liste[k+1],liste[k]
            print (liste)
print(liste)
