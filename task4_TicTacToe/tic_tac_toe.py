class Cell:
    """Клетка"""

    def __init__(self, cell_num: int):
        self.value: str = " "  # значение в клетке
        self.number: int = cell_num  # номер клетки


class Board:
    """Класс поля, который создаёт у себя экземпляры клетки"""

    def __init__(self):
        self.field = [Cell(i) for i in range(1, 10)]

    def print_board(self):
        print("-" * 13)
        cell_string: str = "|"
        for i in range(3):
            for j in range(3):
                cell_string = cell_string + " {cell_num} |".format(cell_num=self.field[j + i * 3].number)
            print(cell_string)
            print("-" * 13)
            cell_string: str = "|"

    def fill_board(self):
        print("-" * 13)
        cell_string: str = "|"
        for i in range(3):
            for j in range(3):
                cell_string = cell_string + " {cell_val} |".format(cell_val=self.field[j + i * 3].value)
            print(cell_string)
            print("-" * 13)
            cell_string: str = "|"


class Player:
    """Игрок"""

    def __init__(self, name: str, role: str):
        self.name: str = name  # имя игрока
        self.role: str = role
        self.winner: bool = False


class Game:
    """Игра"""
    INPUT_ERROR: str = "Некорректный номер клетки! Введите номер клетки от 1 до 9."
    BUSY_CELL_ERROR: str = "Клетка {cell_num} занята. Выберите другую."
    GAME_OVER: str = "Игра завершена.\nИгрок Х {x_name} {x_result}.\nИгрок O {o_name} {o_result}."

    def __init__(self, x_name: str, o_name: str):
        self.board = Board()
        self.player_X = Player(x_name, "X")
        self.player_O = Player(o_name, "O")
        self.victory: bool = False

    def move(self, player):
        res = False
        try:
            target_cell: int = int(input("{player}, введите номер клетки (от 1 до 9):".format(player=player.name)))
            if 1 <= target_cell <= 9:
                if board.field[target_cell - 1].value == " ":
                    board.field[target_cell - 1].value = player.role
                    res = True
                else:
                    print(self.BUSY_CELL_ERROR.format(cell_num=target_cell))
            else:
                print(self.INPUT_ERROR)
        except ValueError:
            print(self.INPUT_ERROR)
        return res

    def decide_victory(self):
        win_combs_list = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),
                          (0, 4, 8), (2, 4, 6)]
        for comb in win_combs_list:
            # if all(self.board.field[cell].number == self.board.field[comb[0]].number for cell in comb):
            if self.board.field[comb[0]].value == self.board.field[comb[1]].value == self.board.field[comb[2]].value!=" ":
                self.victory = True
            # если в выигрышной комбинации все клетки заняты одинаковым значением
            # if self.board.field[comb[0]].number == self.board.field[comb[0]].number == self.board.field[comb[0]].number:
            #     self.victory = True

    def game_result(self, player) -> str:
        if player.winner:
            result: str = "победил"
        else:
            result = "проиграл"
        return result

    def play(self):
        players_list = [self.player_X, self.player_O]
        while not self.victory:
            if any(cell.value == " " for cell in self.board.field):
                for player in players_list:
                    while not self.move(player):
                        self.move(player)
                    else:
                        board.fill_board()
                        self.decide_victory()
                        player.winner = self.victory
            else:
                print("Ничья!")
        else:
            print(self.GAME_OVER.format(x_name=self.player_X.name, x_result=self.game_result(self.player_X),
                                        o_name=self.player_O.name, o_result=self.game_result(self.player_O)))


if __name__ == '__main__':
    board = Board()
    board.print_board()

    player_X_name = input("\nВведите имя игрока X:")
    player_O_name = input("\nВведите имя игрока O:")

    game = Game(player_X_name, player_O_name)
    game.play()
