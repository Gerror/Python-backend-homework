import unittest
from custom_list import CustomList


class TestCustomList(unittest.TestCase):
    def setUp(self) -> None:
        self.custom_list_1 = CustomList([1, 2, 3])
        self.custom_list_2 = CustomList([7, 10, 12, 14])
        self.custom_list_3 = CustomList([4, 2])
        self.custom_list_4 = CustomList([3, 4, 5])

    def test_add_list_and_custom_list(self):
        result = [2, 15, 5, 4] + self.custom_list_1
        self.assertIsInstance(result, CustomList)

        list_sum = list(result)
        self.assertEqual(list_sum, [3, 17, 8, 4])

        self.assertEqual(list(self.custom_list_1), [1, 2, 3])

    def test_add_custom_list_and_list(self):
        result = self.custom_list_1 + [2, 15, 5, 4]
        self.assertIsInstance(result, CustomList)

        list_sum = list(result)
        self.assertEqual(list_sum, [3, 17, 8, 4])

        self.assertEqual(list(self.custom_list_1), [1, 2, 3])

    def test_add_custom_list_and_custom_list(self):
        result = self.custom_list_1 + self.custom_list_2
        self.assertIsInstance(result, CustomList)

        list_sum = list(result)
        self.assertEqual(list_sum, [8, 12, 15, 14])

        result = self.custom_list_1 + self.custom_list_4
        self.assertIsInstance(result, CustomList)

        list_sum = list(result)
        self.assertEqual(list_sum, [4, 6, 8])

        self.assertEqual(list(self.custom_list_1), [1, 2, 3])
        self.assertEqual(list(self.custom_list_2), [7, 10, 12, 14])
        self.assertEqual(list(self.custom_list_4), [3, 4, 5])

    def test_sub_list_and_custom_list(self):
        result = [2, 15, 5, 4] - self.custom_list_1
        self.assertIsInstance(result, CustomList)

        list_sub = list(result)
        self.assertEqual(list_sub, [1, 13, 2, 4])

        self.assertEqual(list(self.custom_list_1), [1, 2, 3])

    def test_sub_custom_list_and_list(self):
        result = self.custom_list_1 - [2, 15, 5, 4]
        self.assertIsInstance(result, CustomList)

        list_sub = list(result)
        self.assertEqual(list_sub, [-1, -13, -2, -4])

        self.assertEqual(list(self.custom_list_1), [1, 2, 3])

    def test_sub_custom_list_and_custom_list(self):
        result = self.custom_list_1 - self.custom_list_2
        self.assertIsInstance(result, CustomList)
        self.assertEqual(list(result), [-6, -8, -9, -14])

        list_sub = list(self.custom_list_2 - self.custom_list_1)
        self.assertEqual(list_sub, [6, 8, 9, 14])

        self.assertEqual(list(self.custom_list_1), [1, 2, 3])
        self.assertEqual(list(self.custom_list_2), [7, 10, 12, 14])

    def test_lt(self):
        self.assertTrue(self.custom_list_1 < self.custom_list_2)
        self.assertTrue(self.custom_list_1 < [1, 6])

    def test_le(self):
        self.assertTrue(self.custom_list_1 <= self.custom_list_3)
        self.assertTrue(self.custom_list_1 <= self.custom_list_2)
        self.assertTrue(self.custom_list_1 <= [3, 2, 1])

    def test_eq(self):
        self.assertTrue(self.custom_list_1 == self.custom_list_3)
        self.assertTrue(self.custom_list_1 == [3, 2, 1])

    def test_ne(self):
        self.assertTrue(self.custom_list_1 != self.custom_list_2)
        self.assertFalse(self.custom_list_1 != self.custom_list_3)
        self.assertTrue(self.custom_list_1 != [3, 2, 10])

    def test_gt(self):
        self.assertTrue(self.custom_list_2 > self.custom_list_1)
        self.assertTrue(self.custom_list_2 > [7, 7, 7, 7])

    def test_ge(self):
        self.assertTrue(self.custom_list_1 >= self.custom_list_3)
        self.assertTrue(self.custom_list_2 >= self.custom_list_1)
        self.assertTrue(self.custom_list_2 >= [7, 7, 7, 7])

    def test_invert(self):
        new_custom_list = CustomList(self.custom_list_1.copy())
        new_custom_list.invert()
        self.assertEqual(list(new_custom_list), [-1, -2, -3])


if __name__ == '__main__':
    unittest.main()
