"""
Модуль с метаклассом, который добавляет к именам
всех атрибутов и функций класса префикс custom_
"""


class CustomMeta(type):
    """
    Метакласса, добавляющий префикс custom_
    """
    @staticmethod
    def change_attr_name(attr_name, class_name):
        """
        Добавляет к атрибуту префикс custom_,
        если это не магический метод или не
        псевдоприватная переменная
        :param attr_name: имя атрибута
        :param class_name: имя класса
        :return: измененное имя атрибута
        """
        result = ""
        if (attr_name.startswith('__') and attr_name.endswith('__')) or \
                attr_name.startswith(f'_{class_name}'):
            result = attr_name
        else:
            result = f"custom_{attr_name}"
        return result

    def __new__(cls, class_name, class_parents, class_attr):
        custom_class_attr = {}
        for name, value in class_attr.items():
            custom_class_attr[CustomMeta.change_attr_name(name, class_name)] = value
        return super().__new__(cls, class_name, class_parents, custom_class_attr)


class CustomClass(metaclass=CustomMeta):
    """
    Класс для тестирования метакласса
    CustomMeta
    """
    x = 50
    __private_var1 = 10

    def __init__(self, arg, val=99):
        self.val = val
        self.arg = arg
        self.__private_var2 = 2

    def __setattr__(self, key, value):
        super().__setattr__(CustomMeta.change_attr_name(key, CustomClass.__name__), value)

    @staticmethod
    def line():
        return 100
