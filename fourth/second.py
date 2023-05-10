from sympy import sin, cos
import numpy as np
from utp_extensions import newton_method, build_graph, BaseAction


class Action(BaseAction):
    @classmethod
    def f(cls, x):
        return sin(x)-x**2*cos(x)

    @classmethod
    def exec(cls):
        print(newton_method(cls.f, 5))
        x = np.arange(-5, 5, 0.01)
        build_graph(cls.f, x)
