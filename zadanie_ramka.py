
def ramki():
    tab = list(map(lambda x:int(x), input().split()))
    n = len(tab)
    k= int(input())
    print("Tablica: ",tab)
    print ("Ilość liczb w tablicy: ",n)
    print("Długość ramki: ",k)
    # tablica do odkładania ramek z tablicy
    C=[]
    # tablica do odkładania różnic pomiędzy największą i najmniejszą wartością
    D=[]
    i=0
    while i<=n-k:
        C.append(tab[i:(k+i)])
        D.append(max(C[i])-min(C[i]))
        i+=1
    # print(C)
    print("Maksymalna różnica wartości w podanych przykładach wynosi: ",max(D))
ramki()

