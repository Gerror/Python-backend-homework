"""
Модуль с игрой в крестики-нолики.
"""


class TicTacToeGame:
    """
    Класс для игры в крестики-нолики.
    """

    def __init__(self):
        self.board = list(range(1, 10))
        self.current_player = 0
        self.symbols = {0: "X", 1: "O"}

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
                raise ValueError("Invalid input. "
                                 "Input must be a number from 1 to 9.")
            current_input = current_input - 1

            if self.board[current_input] in self.symbols.values():
                raise ValueError("Invalid input. "
                                 "The selected cell is already occupied")

            return True
        except ValueError as error:
            print(error)
            return False

    def set_cell(self, current_input):
        """
        Устанавливет символ в ячейку
        :param current_input: Пользовательский ввод
        :return: True, если удалось в выбранную клетку поставить соответствующий
        пользователю символ и False иначе.
        """
        valid_input = self.validate_input(current_input)
        if valid_input:
            self.board[current_input - 1] = self.symbols[self.current_player]
            return True
        return False

    def start_game(self):
        """
        Запускает игру.
        """
        self.show_board()
        there_is_winner = False
        step_counter = 0
        while not there_is_winner and step_counter < 9:
            step_counter += 1
            try:
                print("Choose where to put "
                      f"{self.symbols[self.current_player]}")

                cell_is_set = False
                while not cell_is_set:
                    current_input = input()
                    cell_is_set = self.set_cell(int(current_input))

                self.show_board()
                if self.check_winner():
                    there_is_winner = True
                    break
                self.current_player = (self.current_player + 1) % 2
            except KeyboardInterrupt:
                print("End game")
                break
        if not there_is_winner:
            print("Draw")

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
                print(f"Player {self.symbols[self.current_player]} win")
                return True
        return False


if __name__ == '__main__':
    game = TicTacToeGame()
    game.start_game()
