import unittest
from tic_tac_toe_game import TicTacToeGame


class TestTicTacToeGame(unittest.TestCase):
    def setUp(self) -> None:
        self.tic_tac_toe_game = TicTacToeGame()
        self.tic_tac_toe_game_win_x = TicTacToeGame(["X", "X", "O",
                                                     "X", "O", "O",
                                                     "X", "O", "X"])
        self.tic_tac_toe_game_draw = TicTacToeGame(["X", "O", "X",
                                                    "X", "O", "O",
                                                    "O", "X", "X"])

    def test_valid_input(self):
        for i in range(1, 10):
            self.assertTrue(self.tic_tac_toe_game.validate_input(str(i)))

    def test_invalid_input(self):
        self.assertFalse(self.tic_tac_toe_game.validate_input("-1"))
        self.assertFalse(self.tic_tac_toe_game.validate_input("str"))
        self.assertFalse(self.tic_tac_toe_game.validate_input("1.42"))
        self.assertFalse(self.tic_tac_toe_game.validate_input("10"))
        self.assertFalse(self.tic_tac_toe_game.validate_input("a"))

    def test_check_winner(self):
        self.assertEqual(self.tic_tac_toe_game_win_x.check_winner(), "X")
        self.assertEqual(self.tic_tac_toe_game_draw.check_winner(), "Draw")


if __name__ == '__main__':
    unittest.main()
