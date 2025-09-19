# Method Resolution Order (MRO)
# Defines the order in which Python looks up methods and attributes in classes during inheritance_abstraction.

class A:
    num = 100

class B(A):
    pass

class C(A):
    num = 20

class D(B, C):
    pass

print(D.num)  
print(C.num)
print(B.num)
print(A.num)

print(D.mro()) # Gives D's order of method resolution
