import math

from utp_extensions import BaseAction, build_graph_params
from random import uniform


class Action(BaseAction):
    @classmethod
    def exec(cls):
        x_axis = cls.get_x_axis()
        y_axis = cls.get_y_axis()
        print([complex(x_axis[i], y_axis[i]) for i in range(len(x_axis))])
        build_graph_params(cls.get_x_axis(), cls.get_y_axis(), True)

    @classmethod
    def get_x_axis(cls):
        return [uniform(-5, 5) for _ in range(10)]

    @classmethod
    def get_y_axis(cls):
        return [uniform(-math.pi, math.pi) for _ in range(10)]
