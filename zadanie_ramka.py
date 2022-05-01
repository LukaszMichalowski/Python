
def ramki():
    tab = list(map(lambda x:int(x), input().split()))
    n = len(tab)
    k= int(input())
    print("Tablica: ",tab)
    print ("Ilość liczb w tablicy: ",n)
    print("Długość ramki: ", k)
    i=0
    C=[]
    D=[]
    while i<=n-k:
        C.append(tab[i:(k+i)])
        D.append(max(C[i])-min(C[i]))
        i+=1
        print(C)
      
ramki()

