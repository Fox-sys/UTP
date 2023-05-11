from utp_extensions import BaseAction
import numpy as np
import functools
import math
import fractions


class Action(BaseAction):
    @classmethod
    def exec(cls):
        matrix = np.array([
            [1, 2, 3, 4],
            [2, 3, 1, 2],
            [1, 1, 1, -1],
            [1, 0, -2, -3]]
        )
        # matrix = np.array([[-1, -6], [2, 6]])
        numbers, vectors = np.linalg.eig(matrix)
        print(numbers)
        for vector in vectors:
            print(vector)
