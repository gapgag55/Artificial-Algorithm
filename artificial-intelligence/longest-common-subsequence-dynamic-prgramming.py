def lcs(word, term):
  m = len(word)
  n = len(term)

  L = [[None]*(n+1) for i in range(m+1)]

  for i in range(m+1):
    for j in range(n+1):
      if i == 0 or j == 0:
        L[i][j] = 0
      elif word[i-1] == term[j-1]:
        L[i][j] = L[i-1][j-1] + 1
      else:
        L[i][j] = max(L[i-1][j], L[i][j-1])
  return L[m][n]

word = "FISH"
term = "FOSH"
print("Length of LCS is", lcs(word, term))
