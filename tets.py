class A(object):
    def demo_a(self):
        print("demo-a")


class B():

    def demo_b(self):
        print("demo-b")


class C(A, B):
    def demo_c(self):
        print("demo-c")


c = C()
c.demo_a()
c.demo_b()
c.demo_c()