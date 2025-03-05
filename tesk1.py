n = 5
for i in range(n+1):
    print(" " * (n-i) + " ".join(str(j) for j in range(1, i+1)))
for i in range(n-1):
    print(" " * (i+1) + " ".join(str(j) for j in range(1, n-i)))
