"""
Модуль с кастомным списком, в котором сумма/разность списков
реализована как поэлементная сумма/разность, а сравнение
осуществляется на основе сравнения суммы элементов в списке.
"""


class CustomList(list):
    """
    Кастомный список
    """

    def invert(self):
        """
        Умножает все элементы списка на -1
        """
        for i, element in enumerate(self):
            self[i] = -1 * element

    def sum_list_elements(self):
        """
        :return: Сумма элементов списка
        """
        sum_elements = 0
        for element in self:
            sum_elements += element
        return sum_elements

    def __add__(self, other):
        big = self if len(self) >= len(other) else other
        small = self if len(self) < len(other) else other
        result = CustomList(big.copy())
        for i, element in enumerate(small):
            result[i] += element
        return result

    def __sub__(self, other):
        minus_other = CustomList(other.copy())
        minus_other.invert()
        return self + minus_other

    def __radd__(self, other):
        return self + other

    def __rsub__(self, other):
        result = self - other
        result.invert()
        return result

    def __lt__(self, other):
        other_custom_list = CustomList(other)
        if self.sum_list_elements() < other_custom_list.sum_list_elements():
            return True
        return False

    def __le__(self, other):
        return self < other or self == other

    def __eq__(self, other):
        return not self < other and not self > other

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        return other < self

    def __ge__(self, other):
        return self > other or self == other
