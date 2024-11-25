def newton(vx, vy, x):
    n = len(vx)
    d = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        d[i][0] = vy[i]
    c = n-1
    for j in range(1, n):
        for i in range(0, c):
            d[i][j] = (d[i+1][j-1] - d[i][j-1]) / (vx[i+j] - vx[i])
        c-=1
    pn = vy[0]
    for k in range(1, n):
        pk = d[0][k]
        for j in range(0, k):
            pk *= (x - vx[j])
        pn += pk
    return pn

x = [0, 1, 2, 3, 4]
y = [1, 2, 3, 4, 5]

x_test = 7

print(f"P({x_test}) = {newton(x,y,x_test)}")
