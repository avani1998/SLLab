#one line comprehension 
S = [x for x in range(10)]
M = [x for x in S if x%2 == 0]
M.reverse()
print(S)
print(M)

