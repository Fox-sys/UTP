from utp_extensions import BaseAction


class Action(BaseAction):
    @classmethod
    def exec(cls):
        print(cls.get_polinom() + ['c'])

    @classmethod
    def get_polinom(cls):
        return [1, 2, 3, 4]
