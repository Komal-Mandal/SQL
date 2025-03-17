def change(L):
    print(id(L))
    L = L+(5,6)
    print(L)
    print(id(L))

L1 = (1,2,3,4)
print(L1)
print(id(L1))

change(L1)
print(L1)