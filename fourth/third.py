from utp_extensions import newton_method, BaseAction


class Action(BaseAction):
    f_2 = lambda x: x * 2 ** x - 1

    @classmethod
    def f_1(cls, x):
        return x * 2 ** x - 1

    @classmethod
    def exec(cls):
        print(newton_method(cls.f_1, 5))
        print(newton_method(cls.f_2, 5))
