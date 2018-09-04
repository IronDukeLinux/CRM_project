from django.test import TestCase

# Create your tests here.


class A():

    def a(self, s=None):
        print(s)
        return 'a112'

    def b(self):
        a2 = A.a(self, s=1)
        a3 = self.a(self, s=2)
        return a2, a3

a1 = A()
print(a1.b())

