from utp_extensions import BaseAction, build_graph_params
from math import cos, sin
from numpy import arange


class Action(BaseAction):
    @classmethod
    def exec(cls):
        x = [cls.f_x(2, t) for t in arange(1, 20, 0.01)]
        y = [cls.f_y(2, t) for t in arange(1, 20, 0.01)]
        build_graph_params(x, y)

    @classmethod
    def f_x(cls, a, t):
        return 2 * a * cos(t) * (1 + cos(t))

    @classmethod
    def f_y(cls, a, t):
        return 2 * a * sin(t) * (1 + cos(t))
