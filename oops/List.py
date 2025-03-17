def change(L):
    print(id(L))
    L.append(5)
    print(id(L))

L1 = [1,2,3,4]
print(L1)
print(id(L1))

change(L1[:])
print(L1)
# it is mutable
# by using passby reference if we send mutable datatype then it can change orignal value