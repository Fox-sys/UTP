from utp_extensions import BaseAction
import matplotlib.pyplot as plt
from utp_extensions import TaylorSeries
import numpy as np
import sympy
import matplotlib

matplotlib.use('TkAgg')


class Action(BaseAction):
    @classmethod
    def func(cls, x):
        return sympy.sin(x * 3) ** 3

    def exec(cls):
        start_point = -2
        end_point = 2
        fig, ax = plt.subplots()
        x = np.arange(start_point, end_point, 0.01)
        ax.plot(
            x,
            [cls.func(x_) for x_ in x]
        )
        taylor = TaylorSeries(cls.func, 5, 0)
        print(taylor.get_coefficients())
        ax.plot(
            x,
            [taylor.count_polynom(x_) for x_ in x]
        )
        ax.plot(
            x,
            [abs(cls.func(x_) - taylor.count_polynom(x_)) for x_ in x]
        )
        print(np.roots(taylor.get_coefficients()[::-1]))
        plt.grid()
        plt.show()
