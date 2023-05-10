from utp_extensions import BaseAction
import numpy as np


class Action(BaseAction):
    @classmethod
    def crammer(cls, matrix: np.array, ansers: np.array) -> np.array:
        """
        Функция решения системы уравнений методом крамера
        :param matrix: Мартица коэфициэнтов
        :param ansers: Столбец ответов
        :return: Солбец неизвесных
        """
        D = np.linalg.det(matrix)

        if (D == 0):
            return
        else:
            # список побочных определителей
            dets = []

            for i in range(len(matrix)):
                copied_A = np.array(matrix)
                copied_A[:, i] = ansers
                dets.append(np.linalg.det(copied_A))

            # вектор решений
            x = []
            for curr_det in dets:
                x.append(float(curr_det) / D)

            return x

    @classmethod
    def bubble_max_row(cls, m, k):
        ind = k + np.argmax(np.abs(m[k:, k]))
        if ind != k:
            m[k, :], m[ind, :] = np.copy(m[ind, :]), np.copy(m[k, :])

    @classmethod
    def solve_gauss(cls, m):
        n = m.shape[0]
        for k in range(n - 1):
            cls.bubble_max_row(m, k)
            for i in range(k + 1, n):
                frac = m[i, k] / m[k, k]
                m[i, :] -= m[k, :] * frac

        if cls.is_singular(m):
            print('У системы бесконечное кол-во решений')
            return

        x = np.matrix([0.0 for i in range(n)]).T
        for k in range(n - 1, -1, -1):
            x[k, 0] = (m[k, -1] - m[k, k:n] * x[k:n, 0]) / m[k, k]
        return x

    @classmethod
    def is_singular(cls, m):
        return np.any(np.diag(m) == 0)

    @classmethod
    def reversed_matrix(cls, A: np.array, b: np.array) -> np.array:
        """
        Функция решения системы уравнений методом обратной мартицы
        :param A: Мартица коэфициэнтов
        :param b: Столбец ответов
        :return: Солбец неизвесных
        """
        return np.linalg.inv(A).dot(b)

    @classmethod
    def exec(cls):
        A_list = np.array([
            [0, 2, 3, 4],
            [2, 3, 1, 2],
            [1, 1, 1, -1],
            [1, 0, -1, -1]
        ])
        b_list = np.array([[22, 17, 8, -7]])
        A = []
        for a in A_list:
            A.append(np.array(a, dtype=float))
        B = []
        for b in b_list:
            B.append(np.array(b, dtype=float))
        A = np.array(A)
        B = np.array(B)
        print(cls.crammer(A, B[0]))
        print(cls.reversed_matrix(A, B[0]))
        print(cls.solve_gauss(np.append(A, B.transpose(), axis=1)).reshape(1, 4)[0])
