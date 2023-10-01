from utp_extensions import BaseAction


class Action(BaseAction):
    @classmethod
    def exec(cls):
        print(cls.get_polinom()[0:-1])

    @classmethod
    def get_polinom(cls):
        return [1, 2, 3, 4]
