N = 4
print("The dimension : " + str(N))
res = [list(range(1 + N * i, 1 + N * (i + 1)))
                            for i in range(N)]
print("The created matrix of N * N: " + str(res))
