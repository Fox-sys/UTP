from utp_extensions import BaseAction
import numpy as np


class Action(BaseAction):
    @classmethod
    def exec(cls):
        print(np.roots([2, -9, -60, 1]))
