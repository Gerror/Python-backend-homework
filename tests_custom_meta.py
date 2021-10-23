import unittest
from custom_meta import CustomMeta, CustomClass


class TestCustomMeta(unittest.TestCase):
    def setUp(self) -> None:
        self.custom_class = CustomClass(21)

    def test_get_attribute(self):
        self.assertFalse(hasattr(self.custom_class, "x"))
        self.assertFalse(hasattr(self.custom_class, "val"))
        self.assertFalse(hasattr(self.custom_class, "arg"))
        self.assertFalse(hasattr(self.custom_class, "custom__CustomClass__private_var1"))
        self.assertFalse(hasattr(self.custom_class, "custom__CustomClass__private_var2"))
        self.assertFalse(hasattr(self.custom_class, "line"))

    def test_get_custom_attribute(self):
        self.assertTrue(hasattr(self.custom_class, "custom_x"))
        self.assertTrue(hasattr(self.custom_class, "custom_val"))
        self.assertTrue(hasattr(self.custom_class, "custom_arg"))
        self.assertTrue(hasattr(self.custom_class, "_CustomClass__private_var1"))
        self.assertTrue(hasattr(self.custom_class, "_CustomClass__private_var2"))
        self.assertTrue(hasattr(self.custom_class, "custom_line"))

    def test_values(self):
        self.assertEqual(self.custom_class.custom_x, 50)
        self.assertEqual(self.custom_class.custom_val, 99)
        self.assertEqual(self.custom_class.custom_arg, 21)
        self.assertEqual(self.custom_class._CustomClass__private_var1, 10)
        self.assertEqual(self.custom_class._CustomClass__private_var2, 2)
        self.assertEqual(self.custom_class.custom_line(), 100)


if __name__ == '__main__':
    unittest.main()
