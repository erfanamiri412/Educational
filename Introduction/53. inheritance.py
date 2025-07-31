class A:
    def a(self):
        print('class A.')

class B(A):
    def b(self):
        print('class B.')

class C(B):
    def c(self):
        print('class C.')

c1 = C()
c1.c()
c1.b()
c1.a()


# answer = class C.
#          class B.
#          class A.