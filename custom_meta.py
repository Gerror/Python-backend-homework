"""
Модуль с метаклассом, который добавляет к именам
всех атрибутов и функций класса префикс custom_
"""


class CustomMeta(type):
    """
    Метакласса, добавляющий префикс custom_
    """
    @staticmethod
    def change_dict_names(dictionary, class_name):
        custom_dictionary = {}
        for name, value in dictionary.items():
            if (name.startswith('__') and name.endswith('__')) or \
                    name.startswith(f'_{class_name}'):
                custom_dictionary[name] = value
            else:
                custom_dictionary[f"custom_{name}"] = value
        return custom_dictionary

    def __new__(cls, class_name, class_parents, class_attr):
        custom_class_attr = CustomMeta.change_dict_names(class_attr, class_name)
        return super().__new__(cls, class_name, class_parents, custom_class_attr)

    def __call__(self, *args, **kwargs):
        inst = super().__call__(*args, **kwargs)
        inst.__dict__ = CustomMeta.change_dict_names(inst.__dict__, self.__name__)
        return inst


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

    @staticmethod
    def line():
        return 100
