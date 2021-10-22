import unittest
from custom_meta import CustomMeta, CustomClass


class TestCustomMeta(unittest.TestCase):
    def setUp(self) -> None:
        self.custom_class = CustomClass(21)

    def validate_attribute(self, attr):
        try:
            self.custom_class.__getattribute__(attr)
            return True
        except AttributeError:
            return False


    def test_get_attribute(self):
        attr_list = ["x", "val", "arg", "custom__CustomClass__private_var1",
                     "custom__CustomClass__private_var2", "line"]
        for attr in attr_list:
            res = self.validate_attribute(attr)
            if res:
                self.assertTrue(False)

    def test_get_custom_attribute(self):
        attr_list = ["custom_x", "custom_val", "custom_arg",
                     "_CustomClass__private_var1",
                     "_CustomClass__private_var2", "custom_line"]
        for attr in attr_list:
            res = self.validate_attribute(attr)
            if not res:
                self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
