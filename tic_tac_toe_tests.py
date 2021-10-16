import unittest
from tic_tac_toe_game import TicTacToeGame


class TestTicTacToeGame(unittest.TestCase):
    def setUp(self) -> None:
        self.tic_tac_toe_game = TicTacToeGame()

    def test_valid_input(self):
        for i in range(1, 10):
            self.assertTrue(self.tic_tac_toe_game.validate_input(str(i)))

    def test_invalid_input(self):
        self.assertFalse(self.tic_tac_toe_game.validate_input("-1"))
        self.assertFalse(self.tic_tac_toe_game.validate_input("str"))
        self.assertFalse(self.tic_tac_toe_game.validate_input("1.42"))
        self.assertFalse(self.tic_tac_toe_game.validate_input("10"))

    def test_double_input(self):
        for i in range(1, 10):
            self.assertTrue(self.tic_tac_toe_game.set_cell(i))
            self.assertFalse(self.tic_tac_toe_game.set_cell(i))


if __name__ == '__main__':
    unittest.main()
