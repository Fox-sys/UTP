import math

from utp_extensions import BaseAction, build_graph_params
from random import uniform


class Action(BaseAction):
    @classmethod
    def exec(cls):
        build_graph_params(cls.get_x_axis(), cls.get_y_axis(), True)

    @classmethod
    def get_x_axis(cls):
        return [uniform(-5, 5) for _ in range(10)]

    @classmethod
    def get_y_axis(cls):
        return [uniform(-math.pi, math.pi) for _ in range(10)]
