from utp_extensions import BaseAction
import numpy as np
from utp_extensions import build_graph_params


class Action(BaseAction):
    piece_size = 10
    repeat_count = 4

    @classmethod
    def exec(cls):
        build_graph_params(*cls.build_from_pieces())

    @classmethod
    def build_from_pieces(cls):
        pieces = cls.get_pieces()
        f_range = np.array([])
        pieces_amount = len(pieces)
        x_range = np.arange(0, cls.repeat_count * cls.piece_size * pieces_amount - cls.repeat_count)
        for piece in pieces:
            f_range = np.append(f_range, piece())
        final_range = np.array([])
        for _ in range(cls.repeat_count):
            final_range = np.append(final_range, f_range)
        print(final_range)
        return x_range, final_range

    @classmethod
    def get_pieces(cls) -> list:
        return [getattr(cls, i) for i in dir(cls) if "build_piece" in i]

    @classmethod
    def build_piece_1(cls):
        f_range = np.arange(1, cls.piece_size) / 16
        return f_range

    @classmethod
    def build_piece_2(cls):
        f_range = np.arange(0, cls.piece_size) / 16
        return f_range - f_range[-1]
