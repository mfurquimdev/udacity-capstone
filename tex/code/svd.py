m = np.array(
    [[1, 5, 2],
     [4, 7, 4],
     [2, 0, 9]])

# $U\ S\ V^{T} = M$
U, S, VT = np.linalg.svd(m)

print("Getting SVD outputs:-\n")
print("U:\n", U, "\n")
print("S:\n", S, "\n")
print("VT:\n", VT, "\n")

# Getting SVD outputs:
#
# U:  [[ 0.3831556  -0.39279153  0.83600634]
#      [ 0.68811254 -0.48239977 -0.54202545]
#      [ 0.61619228  0.78294653  0.0854506 ]]
#
# S:  [ 12.10668383   6.91783499   1.25370079]
#
# VT:  [[ 0.36079164  0.55610321  0.74871798]
#       [-0.10935467 -0.7720271   0.62611158]
#       [-0.92621323  0.30777163  0.21772844]]
