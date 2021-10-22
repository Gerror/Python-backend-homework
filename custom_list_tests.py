import unittest
from custom_list import CustomList


class TestCustomList(unittest.TestCase):
    def setUp(self) -> None:
        self.custom_list_1 = CustomList([1, 2, 3])
        self.custom_list_2 = CustomList([7, 10, 12, 14])
        self.custom_list_3 = CustomList([4, 2])

    def test_add_list_and_custom_list(self):
        result = [2, 15, 5, 4] + self.custom_list_1
        self.assertTrue(type(result) is CustomList)

        list_sum = list(result)
        self.assertEqual(list_sum, [3, 17, 8, 4])

    def test_add_custom_list_and_list(self):
        result = self.custom_list_1 + [2, 15, 5, 4]
        self.assertTrue(type(result) is CustomList)

        list_sum = list(result)
        self.assertEqual(list_sum, [3, 17, 8, 4])

    def test_add_custom_list_and_custom_list(self):
        result = self.custom_list_1 + self.custom_list_2
        self.assertTrue(type(result) is CustomList)

        list_sum = list(result)
        self.assertEqual(list_sum, [8, 12, 15, 14])

    def test_sub_list_and_custom_list(self):
        result = [2, 15, 5, 4] - self.custom_list_1
        self.assertTrue(type(result) is CustomList)

        list_sub = list(result)
        self.assertEqual(list_sub, [1, 13, 2, 4])

    def test_sub_custom_list_and_list(self):
        result = self.custom_list_1 - [2, 15, 5, 4]
        self.assertTrue(type(result) is CustomList)

        list_sub = list(result)
        self.assertEqual(list_sub, [-1, -13, -2, -4])

    def test_sub_custom_list_and_custom_list(self):
        result = self.custom_list_1 - self.custom_list_2
        self.assertTrue(type(result) is CustomList)
        self.assertEqual(list(result), [-6, -8, -9, -14])

        list_sub = list(self.custom_list_2 - self.custom_list_1)
        self.assertEqual(list_sub, [6, 8, 9, 14])

    def test_lt(self):
        result = self.custom_list_1 < self.custom_list_2
        self.assertTrue(result)

    def test_le(self):
        result = self.custom_list_1 <= self.custom_list_3
        self.assertTrue(result)

        result = self.custom_list_1 < self.custom_list_2
        self.assertTrue(result)

    def test_eq(self):
        result = self.custom_list_1 == self.custom_list_3
        self.assertTrue(result)

    def test_ne(self):
        result = self.custom_list_1 != self.custom_list_2
        self.assertTrue(result)

        result = self.custom_list_1 != self.custom_list_3
        self.assertFalse(result)

    def test_gt(self):
        result = self.custom_list_2 > self.custom_list_1
        self.assertTrue(result)

    def test_ge(self):
        result = self.custom_list_1 >= self.custom_list_3
        self.assertTrue(result)

        result = self.custom_list_2 > self.custom_list_1
        self.assertTrue(result)

    def test_invert(self):
        new_custom_list = CustomList(self.custom_list_1.copy())
        new_custom_list.invert()
        self.assertEqual(list(new_custom_list), [-1, -2, -3])

    def test_sum_elements(self):
        self.assertEqual(self.custom_list_1.sum_list_elements(), 6)


if __name__ == '__main__':
    unittest.main()
