def change_loc():
    n = int(input())
    m = list(map(int, input().split(' ')))
    a = list(map(lambda x: int(x)-1, input().split(' ')))
    b = list(map(lambda x: int(x)-1, input().split(' ')))
    p = [0 for i in range(n)]
    for i in range(n):
        p[b[i]] = a[i]
    C = []
    vis = [False for i in range(n)]
    for i in range(n):
        if i!= vis[i]:
            c = [i]
            vis[i] = True
            x = p[i]
            while vis[x] is not True:
                vis[x] = True
                c.append(x)
                x = p[x]
            C.append(c)
    mass_sum = [sum([m[s] for s in c]) for c in C]
    min_c = [min([m[s] for s in c]) for c in C]
    min_all = min(m)
    w = 0
    for Ci, c in enumerate(C):
        metoda_1 = mass_sum[Ci] + (len(c) - 2) * min_c[Ci]
        metoda_2 = mass_sum[Ci] + min_c[Ci] + (len(c) + 1) * min_all
        w += min(metoda_1, metoda_2)
    print(w)

change_loc()
