"""
Модуль с игрой в крестики-нолики.
"""


class TicTacToeGame:
    """
    Класс для игры в крестики-нолики.
    """

    def __init__(self, board=None):
        if board:
            self.board = board
        else:
            self.board = list(range(1, 10))

    def show_board(self):
        """
        Метод для рисования игрового поля
        """
        print("-------------")
        for i in range(3):
            print("| "
                  f"{self.board[0 + i * 3]} | "
                  f"{self.board[1 + i * 3]} | "
                  f"{self.board[2 + i * 3]} |")
            print("-------------")

    def validate_input(self, current_input):
        """
        Валидирование пользовательского ввода.
        :param пользовательский ввод
        :return: True, если current_input - целое число от 1 до 9
        и False иначе
        """
        try:
            current_input = int(current_input)

            if not 1 <= current_input <= 9:
                raise ValueError("Input must be a number from 1 to 9.")
            current_input = current_input - 1

            if self.board[current_input] in ["X", "O"]:
                raise ValueError("The selected cell is already occupied")

            return True
        except ValueError as error:
            print(f"Invalid input. {error}")
            return False

    def start_game(self):
        """
        Запускает игру.
        """
        there_is_winner = False
        current_player = 0
        symbols = ["X", "O"]

        self.show_board()
        while not there_is_winner:
            try:
                print("Choose where to put "
                      f"{symbols[current_player]}")

                valid_input = False
                current_input = None
                while not valid_input:
                    current_input = input()
                    valid_input = self.validate_input(current_input)

                self.board[int(current_input) - 1] = symbols[current_player]

                self.show_board()
                result = self.check_winner()
                if result != "GameNotOver":
                    if result != "Draw":
                        print(f"Player {result} win")
                    else:
                        print(result)
                    break

                current_player = (current_player + 1) % 2
            except KeyboardInterrupt:
                print("End game")
                break

    def check_winner(self):
        """
        Проверяет игровое поле на наличие выиграшной комбинации.
        :return: True, если есть выиграшная комбинация и False иначе.
        """
        win_combinations = [(0, 1, 2), (3, 4, 5),
                            (6, 7, 8), (0, 3, 6),
                            (1, 4, 7), (2, 5, 8),
                            (0, 4, 8), (2, 4, 6)]
        for combination in win_combinations:
            if self.board[combination[0]] == \
                    self.board[combination[1]] == \
                    self.board[combination[2]]:
                return self.board[combination[0]]

        for i in range(1, 10):
            if i in self.board:
                return "GameNotOver"

        return "Draw"


if __name__ == '__main__':
    game = TicTacToeGame()
    game.start_game()
