
class A:
    def show(self):
        print("Class A")

class B(A):
    def display(self):
        print("Class B")

class C(A):
    def display1(self):
        print("Class C")

class D(B, C):
    def result(self):
        print("Class D")

obj = D()
obj.show()
obj.display()
obj.display1()
obj.result()
