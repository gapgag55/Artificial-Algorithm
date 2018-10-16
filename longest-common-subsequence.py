def lcs(word, term, i, j):
  if i == 0 or j == 0:
    return 0
  elif word[i-1] == term[j-1]:
    return 1 + lcs(word, term, i-1, j-1)
  else:
    return max(lcs(word, term, i, j-1), lcs(word, term, i-1, j))

word = "FISH"
term = "FOSH"

print("Length of LCS is", lcs(word, term, len(word), len(term)))