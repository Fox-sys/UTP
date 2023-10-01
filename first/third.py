from utp_extensions import BaseAction
import numpy as np


class Action(BaseAction):
    @classmethod
    def exec(cls):
        print(np.polyadd([2, -9, -60, 1], [1, 0, 0, 1, -1]))
