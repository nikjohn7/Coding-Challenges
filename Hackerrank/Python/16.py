def biggerIsGreater(w):
    J = -1
    for i in range( len(w)-1, 0, -1 ):
        for j in range( i-1, J, -1 ):
            if w[i] > w[j] : I,J = i,j ; break
    if J == -1 : return "no answer"
    return w[:J]+w[I]+''.join(sorted(w[J:I]+w[I+1:]))