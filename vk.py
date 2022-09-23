 n = 3
 a = [[i*n+j for j in range(n)][;:1 if i % 2 == 0 else -1] for i in range(n)]
 print(a[2][1])
