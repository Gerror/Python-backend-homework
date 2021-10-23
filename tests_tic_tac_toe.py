import unittest
from tic_tac_toe_game import TicTacToeGame


class TestTicTacToeGame(unittest.TestCase):
    def setUp(self) -> None:
        self.tic_tac_toe_game = TicTacToeGame()
        self.tic_tac_toe_game_win_x_1_4_7 = TicTacToeGame(["X", "X", "O",
                                                           "X", "O", "O",
                                                           "X", "O", "X"])
        self.tic_tac_toe_game_win_x_2_5_8 = TicTacToeGame(["X", "X", "O",
                                                           "O", "X", "O",
                                                           "O", "X", "X"])
        self.tic_tac_toe_game_win_x_3_6_9 = TicTacToeGame(["O", "X", "X",
                                                           "O", "O", "X",
                                                           "X", "O", "X"])
        self.tic_tac_toe_game_win_x_1_2_3 = TicTacToeGame(["X", "X", "X",
                                                           "X", "O", "O",
                                                           "O", "O", "X"])
        self.tic_tac_toe_game_win_x_4_5_6 = TicTacToeGame(["X", "O", "O",
                                                           "X", "X", "X",
                                                           "O", "O", "X"])
        self.tic_tac_toe_game_win_x_7_8_9 = TicTacToeGame(["X", "O", "O",
                                                           "O", "O", "X",
                                                           "X", "X", "X"])
        self.tic_tac_toe_game_win_x_3_5_7 = TicTacToeGame(["X", "O", "X",
                                                           "O", "X", "X",
                                                           "X", "O", "O"])
        self.tic_tac_toe_game_win_x_1_5_9 = TicTacToeGame(["X", "O", "O",
                                                           "O", "X", "X",
                                                           "X", "O", "X"])
        self.tic_tac_toe_game_win_o_1_4_7 = TicTacToeGame(["O", "O", "X",
                                                           "O", "X", "X",
                                                           "O", "X", "O"])
        self.tic_tac_toe_game_win_o_2_5_8 = TicTacToeGame(["O", "O", "X",
                                                           "X", "O", "X",
                                                           "X", "O", "O"])
        self.tic_tac_toe_game_win_o_3_6_9 = TicTacToeGame(["X", "O", "O",
                                                           "X", "X", "O",
                                                           "O", "X", "O"])
        self.tic_tac_toe_game_win_o_1_2_3 = TicTacToeGame(["O", "O", "O",
                                                           "O", "X", "X",
                                                           "X", "X", "O"])
        self.tic_tac_toe_game_win_o_4_5_6 = TicTacToeGame(["O", "X", "X",
                                                           "O", "O", "O",
                                                           "X", "X", "O"])
        self.tic_tac_toe_game_win_o_7_8_9 = TicTacToeGame(["O", "X", "X",
                                                           "X", "X", "O",
                                                           "O", "O", "O"])
        self.tic_tac_toe_game_win_o_3_5_7 = TicTacToeGame(["O", "X", "O",
                                                           "X", "O", "O",
                                                           "O", "X", "X"])
        self.tic_tac_toe_game_win_o_1_5_9 = TicTacToeGame(["O", "X", "X",
                                                           "X", "O", "O",
                                                           "O", "X", "O"])
        self.tic_tac_toe_game_draw = TicTacToeGame(["X", "O", "X",
                                                    "X", "O", "O",
                                                    "O", "X", "X"])
        self.tic_tac_toe_game_double_set = TicTacToeGame(["X", "2", "3",
                                                          "4", "5", "6",
                                                          "7", "8", "9"])

    def test_valid_input(self):
        for i in range(1, 10):
            self.assertTrue(self.tic_tac_toe_game.validate_input(str(i)))

    def test_invalid_input(self):
        self.assertFalse(self.tic_tac_toe_game.validate_input("-1"))
        self.assertFalse(self.tic_tac_toe_game.validate_input("0"))
        self.assertFalse(self.tic_tac_toe_game.validate_input("str"))
        self.assertFalse(self.tic_tac_toe_game.validate_input("1.42"))
        self.assertFalse(self.tic_tac_toe_game.validate_input("10"))
        self.assertFalse(self.tic_tac_toe_game.validate_input("a"))

    def test_check_winner(self):
        self.assertEqual(self.tic_tac_toe_game_win_x_1_4_7.check_winner(), "X")
        self.assertEqual(self.tic_tac_toe_game_win_x_2_5_8.check_winner(), "X")
        self.assertEqual(self.tic_tac_toe_game_win_x_3_6_9.check_winner(), "X")
        self.assertEqual(self.tic_tac_toe_game_win_x_4_5_6.check_winner(), "X")
        self.assertEqual(self.tic_tac_toe_game_win_x_7_8_9.check_winner(), "X")
        self.assertEqual(self.tic_tac_toe_game_win_x_3_5_7.check_winner(), "X")
        self.assertEqual(self.tic_tac_toe_game_win_x_1_5_9.check_winner(), "X")
        self.assertEqual(self.tic_tac_toe_game_win_x_1_2_3.check_winner(), "X")
        self.assertEqual(self.tic_tac_toe_game_win_o_1_4_7.check_winner(), "O")
        self.assertEqual(self.tic_tac_toe_game_win_o_2_5_8.check_winner(), "O")
        self.assertEqual(self.tic_tac_toe_game_win_o_3_6_9.check_winner(), "O")
        self.assertEqual(self.tic_tac_toe_game_win_o_4_5_6.check_winner(), "O")
        self.assertEqual(self.tic_tac_toe_game_win_o_7_8_9.check_winner(), "O")
        self.assertEqual(self.tic_tac_toe_game_win_o_3_5_7.check_winner(), "O")
        self.assertEqual(self.tic_tac_toe_game_win_o_1_5_9.check_winner(), "O")
        self.assertEqual(self.tic_tac_toe_game_win_o_1_2_3.check_winner(), "O")
        self.assertEqual(self.tic_tac_toe_game_draw.check_winner(), "Draw")

    def test_double_set(self):
        self.assertFalse(self.tic_tac_toe_game_double_set.validate_input("1"))


if __name__ == '__main__':
    unittest.main()
