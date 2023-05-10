from utp_extensions import BaseAction
import numpy as np


class Action(BaseAction):
    @classmethod
    def exec(cls):
        matrix = [[1, 0, 4], [-5, 3, 3], [2, -2, 0]]
        basis = cls.gram_shmidt(matrix)
        print(basis)
        print("Проверка на ортогональность")
        print(np.dot(basis[0, :], basis[1, :]))
        print(np.dot(basis[1, :], basis[2, :]))
        print(np.dot(basis[2, :], basis[0, :]))


    @classmethod
    def gram_shmidt(cls, matrix):
        vector_len = len(matrix[0])
        vector_amount = len(matrix)
        basis = [[0] * vector_len for i in range(vector_amount)]
        basis[0] = matrix[0]
        for i in range(1, vector_amount):
            sum = matrix[i]
            for j in range(0, i):
                scolar_ab = 0
                scolar_bb = 0
                proj = [i for i in range(vector_len)]
                for n in range(vector_len):
                    scolar_ab += basis[j][n] * matrix[i][n]
                    scolar_bb += basis[j][n] * basis[j][n]
                for n in range(vector_len):
                    proj[n] = (scolar_ab / scolar_bb) * basis[j][n]
                for n in range(vector_len):
                    sum[n] -= proj[n]
            basis[i] = sum
        return np.array(basis)
