class Alpha:
    def fun1(self):
        print("i am an alpha")
class Beta(Alpha):
     def fun2(self):
         print("i am beta")
class Gamma3(Alpha):
    def fun3(self):
        print("i am gamma")
b=Beta()
b.fun1()
b.fun2()
