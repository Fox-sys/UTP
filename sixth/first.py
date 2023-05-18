from utp_extensions import BaseAction
from math import exp, sin


class Action(BaseAction):
    @classmethod
    def exec(cls):
        print(cls.integrate(cls.f, 0, 5))

    @classmethod
    def _integrate_base(cls, f, a, b, n):
        h = (b - a) / float(n)
        total = sum([f((a + (k * h))) for k in range(0, n)])
        result = h * total
        return result

    @classmethod
    def integrate(cls, f, a, b):
        n = 2
        a1 = cls._integrate_base(f, a, b, n)
        n *= 2
        a2 = cls._integrate_base(f, a, b, n)

        while abs(a1 - a2) > 0.001:
            n *= 2
            a1 = cls._integrate_base(f, a, b, n)
            n *= 2
            a2 = cls._integrate_base(f, a, b, n)
        return a2

    @classmethod
    def f(cls, x):
        return (x ** 2 - x) * (exp(x) * sin(x))
