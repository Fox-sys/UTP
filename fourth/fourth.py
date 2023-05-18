import numpy

from utp_extensions import BaseAction, build_graph


class Action(BaseAction):
    @classmethod
    def exec(cls):
        a, b = -5, 5
        build_graph(cls.f, numpy.arange(a, b, 0.001))
        print(cls.bis(cls.f, a, b, 0.001))


    @classmethod
    def f(cls, x):
        return x * 2 ** x - 1

    @classmethod
    def bis(cls, f, a, b, eps):
        while abs(f(b) - f(a)) > eps:
            mid = (a + b) / 2
            if f(mid) == 0 or abs(f(mid)) < eps:
                return mid
            elif f(a) * f(mid) < 0:
                b = mid
            else:
                a = mid
        else:
            return
